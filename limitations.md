# Limitations and Falsification

MOLE is an experimental latent-error framework.

## Limitations

- Latent state may be impossible to observe directly.
- Indirect signals may be noisy.
- The chosen deep indicators may be incomplete.
- Surface/deep mismatch can be benign.
- Some masking is intentionally protective.
- Hidden-state inference can overfit incident histories.

## Falsification criteria

MOLE's central hypothesis is weakened if:

1. Standard multivariate anomaly detection matches performance.
2. Observability-gap scoring adds no lead-time benefit.
3. Deep-channel aggregation does not improve precision.
4. Detected latent failures do not predict later visible failures.
5. Results fail on held-out systems.
6. Gains vanish under matched false-alarm rates.

## Claim boundary

MOLE estimates latent error under the supplied measurement model. It does not prove an unseen failure exists without corroborating evidence.
