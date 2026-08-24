from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class MoleConfig:
    gap_threshold: float = 0.25
    min_coverage: float = 0.5

class MoleEvaluator:
    def __init__(self, deep_weights: Optional[Dict[str,float]] = None, config: Optional[MoleConfig] = None):
        self.deep_weights = deep_weights or {}
        self.config = config or MoleConfig()

    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def evaluate(self, surface_health: float, deep_indicators: Dict[str,float]):
        surface_health = self.clip01(surface_health)
        surface_degradation = 1.0 - surface_health

        if not deep_indicators:
            return {
                "surface_health": surface_health,
                "latent_health": 1.0,
                "observability_gap": 0.0,
                "masking_strength": 0.0,
                "coverage": 0.0,
                "hidden_failure": False,
                "contributions": {}
            }

        raw_weights = {}
        for k in deep_indicators:
            raw_weights[k] = max(0.0, self.deep_weights.get(k,1.0))

        total_w = sum(raw_weights.values()) or 1.0
        contributions = {}
        latent_deg = 0.0

        supporting = 0
        for k,v in deep_indicators.items():
            d = self.clip01(v)
            w = raw_weights[k]/total_w
            contributions[k] = w*d
            latent_deg += w*d
            if d > 0.5:
                supporting += 1

        latent_health = 1.0 - latent_deg
        gap = max(0.0, latent_deg - surface_degradation)
        coverage = supporting / len(deep_indicators)

        hidden_failure = (
            gap >= self.config.gap_threshold and
            coverage >= self.config.min_coverage
        )

        return {
            "surface_health": surface_health,
            "latent_health": latent_health,
            "observability_gap": gap,
            "masking_strength": gap,
            "coverage": coverage,
            "hidden_failure": hidden_failure,
            "contributions": contributions
        }
