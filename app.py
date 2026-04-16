from flask import Flask, render_template, send_file
import random
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route('/')
def home():

    instances = []
    total_savings = 0

    # Generate fake cloud data
    for i in range(5):
        cpu = random.randint(1, 100)
        memory = random.randint(10, 100)
        last_active = random.randint(1, 48)
        cost = random.randint(50, 200)

        if cpu < 10 and memory < 20 and last_active > 24:
            action = "STOP"
            savings = cost
        elif cpu < 30:
            action = "RESIZE"
            savings = int(cost * 0.5)
        elif cpu > 80:
            action = "SCALE UP"
            savings = -int(cost * 0.2)
        else:
            action = "OK"
            savings = 0

        total_savings += savings

        instances.append({
            "id": f"i-10{i}",
            "cpu": cpu,
            "memory": memory,
            "last_active": last_active,
            "cost": cost,
            "action": action,
            "savings": savings
        })

    # ---------------- GRAPH GENERATION (FIXED) ----------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(BASE_DIR, "static")

    os.makedirs(static_dir, exist_ok=True)

    cpu_values = [i["cpu"] for i in instances]
    ids = [i["id"] for i in instances]

    plt.figure(figsize=(6, 4))
    plt.bar(ids, cpu_values)
    plt.title("CPU Usage per Instance")
    plt.xlabel("Instance ID")
    plt.ylabel("CPU %")

    plt.savefig(os.path.join(static_dir, "graph.png"))
    plt.close()

    return render_template(
        "index.html",
        instances=instances,
        savings=total_savings
    )


# ---------------- REPORT DOWNLOAD ----------------
@app.route('/report')
def generate_report():

    instances = []
    file_path = "cloud_report.txt"

    for i in range(5):
        cpu = random.randint(1, 100)
        memory = random.randint(10, 100)
        last_active = random.randint(1, 48)
        cost = random.randint(50, 200)

        if cpu < 10 and memory < 20 and last_active > 24:
            action = "STOP"
            savings = cost
        elif cpu < 30:
            action = "RESIZE"
            savings = int(cost * 0.5)
        else:
            action = "OK"
            savings = 0

        instances.append({
            "id": f"i-10{i}",
            "action": action,
            "cost": cost,
            "savings": savings
        })

    total_cost = sum(i["cost"] for i in instances)
    total_savings = sum(i["savings"] for i in instances)

    with open(file_path, "w") as f:
        f.write("CLOUD COST REPORT\n\n")

        for i in instances:
            f.write(f"{i['id']} | {i['action']} | ₹{i['cost']} | Save ₹{i['savings']}\n")

        f.write("\n-----------------\n")
        f.write(f"TOTAL COST: ₹{total_cost}\n")
        f.write(f"TOTAL SAVINGS: ₹{total_savings}\n")

    return send_file(file_path, as_attachment=True)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
