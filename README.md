☁️ Cloud Cost Optimizer (DevOps Project)

A fully automated DevOps project that analyzes cloud instance usage and provides cost optimization suggestions using a Flask web app with CI/CD pipeline using Jenkins and Docker.

🚀 Features

✔ Cloud instance monitoring (CPU, Memory, Cost)  
✔ Auto optimization logic (STOP / RESIZE / SCALE UP)  
✔ Graph generation using Matplotlib  
✔ Downloadable cost report  
✔ Modern dashboard UI  
✔ Docker containerized deployment  
✔ Fully automated CI/CD pipeline  


 🧰 Tech Stack

- Python (Flask)
- Docker
- Jenkins
- GitHub
- Matplotlib
- HTML / CSS


 🔁 CI/CD Pipeline Flow

GitHub → Jenkins → Docker Build → DockerHub → EC2 Deploy → Live Website

---

 🏗️ Architecture Diagram
+-------------+        +-------------+        +--------------+ |   GitHub    |  --->  |   Jenkins   |  --->  |   Docker     | |  (Code)     |        |  Pipeline   |        |  Image Build | +-------------+        +-------------+        +--------------+ | v +--------------+ |  DockerHub   | |  Registry    | +--------------+ | v +--------------+ |     EC2      | | Flask App    | +--------------+ | v +--------------+ |  Live Site   | +--------------+
 
 ⚙️ How to Run Locally
git clone https://github.com/your-username/cloud-cost-optimizer.git
cd cloud-cost-optimizer
pip install -r requirements.txt
python app.py

🐳 Docker Setup
Bash
docker build -t cloud-cost-optimizer .
docker run -d -p 5000:5000 cloud-cost-optimizer

📊 Output
✔ Dashboard with instance data
✔ CPU usage graph
✔ Cost optimization suggestions
✔ Downloadable report

🔐 CI/CD Pipeline Stages
GitHub Push
Jenkins Auto Trigger
Docker Image Build
DockerHub Push
EC2 Deployment
Live Website Update

📌 Project Goal
To simulate real-world DevOps automation where infrastructure cost is optimized using intelligent instance analysis and fully automated deployment pipeline.

Author
Prachi Dhole
DevOps & Cloud Enthusiast 🚀





