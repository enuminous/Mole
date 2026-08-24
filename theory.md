# MOLE Theory

## 1. Problem

Many systems expose only partial state.

Surface telemetry can remain healthy while:
- hidden queues grow,
- internal invariants fail,
- cached state diverges,
- uninstrumented components degrade,
- error correction masks damage,
- retries hide instability,
- delayed failures accumulate.

MOLE focuses on mismatch between observed health and inferred latent health.

## 2. Surface and latent state

Let visible telemetry be:

`y_t`

and latent system state be:

`z_t`

The system may report a surface health score:

`H_surface(y_t)`

while deeper evidence implies:

`H_latent(z_t)`

## 3. Observability gap

Define:

`G_t = H_surface - H_latent`

A large positive `G_t` means the system looks healthier than it appears to be internally.

## 4. Residual-based latent inference

If a predictive model estimates:

`y_hat_t = F(history)`

then residual:

`r_t = y_t - y_hat_t`

may expose hidden structure.

But MOLE should not rely on one residual alone.

## 5. Cross-channel contradiction

Suppose surface KPI `s_t` is nominal while indirect indicators `q_i(t)` degrade.

Candidate latent score:

`L_t = sum_i w_i * anomaly_i(q_i) - alpha * anomaly_surface(s_t)`

A high `L_t` with low surface anomaly is a MOLE target.

## 6. Masking strength

Let hidden degradation be `D_t` and visible degradation be `V_t`.

`M_t = max(0, D_t - V_t)`

High `M_t` indicates strong masking.

## 7. Delayed reveal

If hidden failure becomes visible at time `T_visible` but MOLE first detects it at `T_mole`:

`RevealLead = T_visible - T_mole`

This must be compared at matched false-alarm rate.

## 8. Evidence coverage

MOLE should track how much of the latent score is supported by independent channels.

`Coverage = independent_supporting_channels / expected_channels`

## 9. EFMW interpretation

The EFMW-inspired element is recursive comparison between:
- observed state,
- inferred hidden state,
- cross-channel relations,
- delayed consequences.

## 10. Falsifiable prediction

MOLE should add value where:
- primary telemetry is masked,
- indirect channels retain precursor information,
- errors are delayed,
- hidden state matters.

If standard anomaly detection on all available channels performs equally well, MOLE's added structure is unnecessary.
