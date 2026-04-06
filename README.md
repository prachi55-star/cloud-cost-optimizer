# Smart Cloud Cost Optimizer

## 📌 Project Description
This project analyzes cloud resource usage and suggests cost-saving actions like stopping idle instances or resizing underutilized ones.

## 🚀 Features
- Detect underutilized instances
- Suggest STOP or RESIZE actions
- Calculate estimated daily savings
- API-based backend using Flask

## 🛠 Tech Stack
- Python
- Flask

## 📊 Sample Output
- Instance i-101 → STOP → Save ₹120/day
- Instance i-103 → RESIZE → Save ₹84/day

## 🌐 API Endpoints
- `/` → Home
- `/optimize` → Get optimization results

## 💡 Future Improvements
- Integrate with AWS using Boto3
- Add real-time monitoring
