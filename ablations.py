from mole import MoleEvaluator, MoleConfig

deep = {
    "queue_growth":0.72,
    "retry_rate":0.68,
    "replica_divergence":0.61,
    "correction_load":0.70
}

if __name__ == "__main__":
    full = MoleEvaluator(config=MoleConfig(gap_threshold=0.25,min_coverage=0.5))
    print("full:", full.evaluate(0.95,deep))

    single = MoleEvaluator(
        deep_weights={
            "queue_growth":1.0,
            "retry_rate":0.0,
            "replica_divergence":0.0,
            "correction_load":0.0
        },
        config=MoleConfig(gap_threshold=0.25,min_coverage=0.5)
    )
    print("single-channel-weighted ablation:", single.evaluate(0.95,deep))
