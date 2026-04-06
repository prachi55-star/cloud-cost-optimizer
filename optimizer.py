def optimize_instances(instances):
    results = []
    total_savings = 0

    for instance in instances:
        cpu = instance["cpu"]
        cost = instance["cost"]

        if cpu < 20:
            savings = cost * 24
            action = "STOP"
        elif cpu < 50:
            savings = cost * 12
            action = "RESIZE"
        else:
            savings = 0
            action = "OK"

        total_savings += savings

        results.append({
            "id": instance["id"],
            "cpu": cpu,
            "action": action,
            "savings_per_day": savings
        })

    return results, total_savings
