from mole import MoleEvaluator

evaluator = MoleEvaluator()

surface_health = 0.96

deep = {
    "hidden_queue":0.71,
    "retry_pressure":0.66,
    "replica_mismatch":0.59
}

print(evaluator.evaluate(surface_health, deep))
