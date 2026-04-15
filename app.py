from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Dummy data
    daily_costs = [120, 150, 200, 180, 220, 250, 300]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Total cost
    total_cost = sum(daily_costs)

    # Alert logic
    LIMIT = 500
    alert_message = None
    if total_cost > LIMIT:
        alert_message = f"⚠️ Alert: Monthly cost exceeded ₹{LIMIT}"

    # 📊 Create graph
    plt.figure()
    plt.plot(days, daily_costs, marker='o')
    plt.title("Daily Cloud Cost")
    plt.xlabel("Days")
    plt.ylabel("Cost (₹)")

    # Save graph
    graph_path = "static/cost_graph.png"
    os.makedirs("static", exist_ok=True)
    plt.savefig(graph_path)
    plt.close()

    return render_template(
        "index.html",
        cost=total_cost,
        alert=alert_message,
        graph=graph_path
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
