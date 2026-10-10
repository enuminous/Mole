# MOLE — EFMW Zoo #35

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Mole) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Masked Observation and Latent Error**

MOLE is an experimental EFMW-inspired framework for detecting failures that remain hidden from ordinary observability.

## Core question

> What important error is present in the system even though the visible indicators still look normal?

MOLE is designed for latent-state mismatch: internal degradation, hidden constraint violation, or masked error that does not yet appear in the primary telemetry.

## Primary outputs

- observability gap
- latent-error score
- surface/deep-state divergence
- hidden-failure confidence
- masking strength
- delayed-reveal estimate
- evidence coverage

## Repository contents

- `theory.md`
- `architecture.md`
- `latent_error_model.md`
- `limitations.md`
- `mole.py`
- `benchmark.py`
- `ablations.py`
- `test_mole.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_mole.py
```

## Zoo position

ORCA #34 evaluates coordination across actors.

**MOLE #35 looks underground: it searches for important state that ordinary surface observability is failing to expose.**
