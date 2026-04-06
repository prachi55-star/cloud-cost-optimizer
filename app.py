from flask import Flask

app = Flask(__name__)

instances = [
    {"id": "i-101", "cpu": 10, "cost": 5},
    {"id": "i-102", "cpu": 80, "cost": 10},
    {"id": "i-103", "cpu": 35, "cost": 7}
]

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Cloud Cost Optimizer</title>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                background-color: #0d6efd;
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            button {
                padding: 12px 25px;
                background-color: white;
                color: #0d6efd;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1 style="font-size: 40px;">🚀 Cloud Cost Optimizer</h1>
        <p>Analyze your cloud usage and reduce unnecessary costs</p>

        <br>
        <button onclick="window.location.href='/optimize'">
            Go to Dashboard
        </button>
    </body>
    </html>
    """

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
            "savings": savings
        })

    rows = ""
    for r in results:
        color = "green"
        if r['action'] == "STOP":
            color = "red"
        elif r['action'] == "RESIZE":
            color = "orange"

        rows += f"""
        <tr>
            <td>{r['id']}</td>
            <td>{r['cpu']}%</td>
            <td style="color:{color}; font-weight:bold;">{r['action']}</td>
            <td>${r['savings']}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>Dashboard</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial;
                background-color: #f4f6f9;
            }}

            .header {{
                background-color: #232f3e;
                color: white;
                padding: 15px;
                font-size: 20px;
                text-align: center;
            }}

            .container {{
                padding: 20px;
            }}

            .cards {{
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-bottom: 20px;
            }}

            .card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                width: 220px;
                text-align: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}

            table {{
                width: 80%;
                margin: auto;
                border-collapse: collapse;
                background: white;
                border-radius: 10px;
                overflow: hidden;
            }}

            th {{
                background-color: #0073bb;
                color: white;
                padding: 12px;
            }}

            td {{
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }}

            tr:hover {{
                background-color: #f1f1f1;
            }}

            .back {{
                display: block;
                text-align: center;
                margin-top: 20px;
                font-size: 16px;
                color: #0073bb;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>

    <div class="header">
        ☁️ Cloud Cost Optimizer Dashboard
    </div>

    <div class="container">

        <div class="cards">
            <div class="card">
                <h3>🖥 Instances</h3>
                <p>{len(results)}</p>
            </div>

            <div class="card">
                <h3>💰 Total Savings</h3>
                <p>${total_savings}</p>
            </div>
        </div>

        <table>
            <tr>
                <th>Instance ID</th>
                <th>CPU Usage</th>
                <th>Action</th>
                <th>Savings</th>
            </tr>
            {rows}
        </table>

        <a href="/" class="back">⬅ Back</a>

    </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
