from mole import MoleEvaluator, MoleConfig

def run():
    ev = MoleEvaluator(
        deep_weights={
            "queue_growth":1.0,
            "retry_rate":1.0,
            "replica_divergence":1.0,
            "correction_load":1.0
        },
        config=MoleConfig(gap_threshold=0.25,min_coverage=0.5)
    )

    healthy = ev.evaluate(
        0.95,
        {
            "queue_growth":0.10,
            "retry_rate":0.15,
            "replica_divergence":0.08,
            "correction_load":0.12
        }
    )

    masked = ev.evaluate(
        0.95,
        {
            "queue_growth":0.72,
            "retry_rate":0.68,
            "replica_divergence":0.61,
            "correction_load":0.70
        }
    )

    visible = ev.evaluate(
        0.50,
        {
            "queue_growth":0.72,
            "retry_rate":0.68,
            "replica_divergence":0.61,
            "correction_load":0.70
        }
    )

    return healthy, masked, visible

if __name__ == "__main__":
    for label,r in zip(["healthy","masked","visible"], run()):
        print(label, r)
