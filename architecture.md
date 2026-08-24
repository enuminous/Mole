# MOLE Architecture

## Pipeline

1. Surface Telemetry Ingestor
2. Deep Signal Collector
3. Normalization Layer
4. Latent Degradation Estimator
5. Surface/Deep Divergence Engine
6. Masking Analyzer
7. Evidence Coverage Calculator
8. Delayed-Reveal Tracker
9. Audit Reporter

## Inputs

- visible health metrics
- indirect/deep indicators
- baseline ranges
- optional masking mechanism metadata
- known failure reveal times

## Outputs

```json
{
  "surface_health": 0.95,
  "latent_health": 0.58,
  "observability_gap": 0.37,
  "masking_strength": 0.37,
  "coverage": 0.75,
  "hidden_failure": true
}
```

## Design principle

MOLE should never claim hidden failure solely because one obscure metric looks unusual.

The strongest finding is:

**multiple independent deep indicators degrade while the main visible indicators remain deceptively normal.**

## Integration

WOLF can supply distributed weak-signal evidence.

JELLYFISH can map which hidden failure will propagate.

ELEPHANT can preserve delayed-reveal histories.

SALMON can trace a revealed failure back to its hidden origins.
