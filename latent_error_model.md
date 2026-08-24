# Latent Error Model

## Observation schema

```json
{
  "surface_health": 0.94,
  "queue_depth": 0.62,
  "retry_rate": 0.51,
  "cache_divergence": 0.47,
  "error_correction_load": 0.58
}
```

## Surface health

A high surface score does not guarantee internal health.

## Deep indicators

MOLE may use:
- queue growth
- retry growth
- divergence between replicas
- correction burden
- hidden resource depletion
- mismatch between expected and realized internal states

## Candidate latent degradation

Normalize each deep indicator:

`d_i in [0,1]`

Then:

`D = sum_i w_i d_i`

Surface degradation:

`V = 1 - surface_health`

Observability gap:

`G = max(0, D - V)`

## Hidden-failure condition

Candidate:

`G > theta_G`

and:

`Coverage > theta_C`

## Masking mechanisms

Possible masking sources:
- retries
- redundancy
- caching
- smoothing
- delayed metrics
- aggregation
- error correction

These should be explicitly modeled where possible.
