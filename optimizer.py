instances = [
    {"id": "i-101", "cpu": 10, "cost": 5},
    {"id": "i-102", "cpu": 80, "cost": 10},
    {"id": "i-103", "cpu": 35, "cost": 7}
]

total_savings = 0

for instance in instances:
    cpu = instance["cpu"]
    cost = instance["cost"]

    if cpu < 20:
        savings = cost * 24  # daily saving
        total_savings += savings
        print(f"{instance['id']}: STOP → Save ₹{savings}/day")

    elif cpu < 50:
        savings = cost * 12
        total_savings += savings
        print(f"{instance['id']}: RESIZE → Save ₹{savings}/day")

    else:
        print(f"{instance['id']}: OK → No savings")

print(f"\nTotal Estimated Savings: ₹{total_savings}/day")
