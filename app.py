from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Sample instance data
instances = [
    {"id": "i-101", "cpu": 10, "cost": 5},
    {"id": "i-102", "cpu": 80, "cost": 10},
    {"id": "i-103", "cpu": 35, "cost": 7}
]

# Home route (UI)
@app.route('/')
def home():
    return render_template_string("""
<html>
<head>
    <title>Cloud Cost Optimizer</title>
    <style>
        body {
            background: #0b1f3a;
            color: white;
            font-family: Arial;
            text-align: center;
        }
        h1 {
            margin-top: 20px;
        }
        .card {
            background: #1e3a5f;
            padding: 20px;
            margin: 20px auto;
            width: 80%;
            border-radius: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            color: black;
        }
        th, td {
            padding: 12px;
            border: 1px solid #ddd;
        }
        th {
            background: #007BFF;
            color: white;
        }
        .stop { color: red; font-weight: bold; }
        .resize { color: orange; font-weight: bold; }
        .ok { color: green; font-weight: bold; }

        button {
            padding: 12px 25px;
            background: #28a745;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<h1>☁️ Smart Cloud Cost Optimizer</h1>

<div class="card">
    <button onclick="loadData()">🚀 Optimize Now</button>

    <table id="resultTable">
        <tr>
            <th>Instance ID</th>
            <th>CPU</th>
            <th>Action</th>
            <th>Savings</th>
        </tr>
    </table>

    <h2 id="total"></h2>
</div>

<script>
function loadData() {
    fetch('/optimize')
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("resultTable");

        table.innerHTML = `
        <tr>
            <th>Instance ID</th>
            <th>CPU</th>
            <th>Action</th>
            <th>Savings</th>
        </tr>`;

        data.results.forEach(item => {
            let className = "";
            if (item.action === "STOP") className = "stop";
            else if (item.action === "RESIZE") className = "resize";
            else className = "ok";

            table.innerHTML += `
            <tr>
                <td>${item.id}</td>
                <td>${item.cpu}%</td>
                <td class="${className}">${item.action}</td>
                <td>₹${item.savings_per_day}</td>
            </tr>`;
        });

        document.getElementById("total").innerHTML =
            "💰 Total Savings: ₹" + data.total_savings + "/day";
    });
}
</script>

</body>
</html>
""")

# Optimization API
@app.route('/optimize')
def optimize():
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

    return jsonify({
        "results": results,
        "total_savings": total_savings
    })

if __name__ == '__main__':
    app.run(debug=True)
