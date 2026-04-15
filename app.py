from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Dummy daily costs (you can replace with real AWS data later)
    daily_costs = [120, 150, 200, 180, 220, 250, 300]

    # Calculate total cost
    total_cost = sum(daily_costs)

    # Set limit
    LIMIT = 500

    # Alert logic
    alert_message = None
    if total_cost > LIMIT:
        alert_message = f"⚠️ Alert: Monthly cost exceeded ₹{LIMIT}"

    return render_template(
        "index.html",
        cost=total_cost,
        alert=alert_message,
        daily_costs=daily_costs
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
