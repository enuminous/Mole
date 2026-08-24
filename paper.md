# MOLE: Masked Observation and Latent Error

## Abstract

MOLE is an experimental framework for detecting divergence between visible system health and deeper latent degradation. It combines multiple indirect indicators, explicit observability-gap scoring, masking analysis, and delayed-reveal evaluation.

## 1. Motivation

Surface telemetry can remain reassuring while internal failure accumulates.

This can happen through:
- retries,
- redundancy,
- smoothing,
- delayed metrics,
- caching,
- aggregation.

MOLE evaluates whether the visible layer is systematically overstating system health.

## 2. Model

Surface degradation:

`V = 1 - H_surface`

Latent degradation:

`D = sum_i w_i d_i`

Observability gap:

`G = max(0,D-V)`

Candidate hidden-failure alarm:

`G > theta_G`

and sufficient independent evidence coverage.

## 3. Metrics

- observability gap
- masking strength
- latent health
- evidence coverage
- delayed-reveal lead time
- hidden-failure precision/recall

## 4. Baselines

- multivariate anomaly detection
- residual monitoring
- one-class classifiers
- change-point detection
- hidden Markov/state-space models

## 5. Ablations

- surface only
- one deep channel only
- no weighting
- no coverage requirement
- no masking term
- no delayed-reveal analysis

## 6. Falsification

If conventional multivariate monitoring detects the same hidden failures at equal or better lead time and false-alarm rate, MOLE's added structure is not justified.

## 7. Claim boundary

MOLE estimates latent degradation from indirect evidence. It cannot establish an unseen failure without corroboration.
