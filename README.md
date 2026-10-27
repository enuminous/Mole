# MOLE — EFMW Zoo #35

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Mole) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Core question](#core-question)
- [Primary outputs](#primary-outputs)
- [Repository contents](#repository-contents)
- [Quick start](#quick-start)
- [Zoo position](#zoo-position)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Lynx](https://github.com/enuminous/Lynx) · [Orca](https://github.com/enuminous/Orca) · [Horse](https://github.com/enuminous/Horse) · [Salmon](https://github.com/enuminous/Salmon)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
