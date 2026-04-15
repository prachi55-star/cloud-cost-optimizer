pipeline {
    agent any

    environment {
        APP_DIR = "cloud-cost-optimizer"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/cloud-cost-optimizer.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Stop Old App') {
            steps {
                echo "Stopping old running Flask app (if any)..."
                sh '''
                    pkill -f app.py || true
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo "Starting Flask app..."
                sh '''
                    nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Checking if app is running..."
                sh '''
                    sleep 5
                    ps -ef | grep app.py | grep -v grep || echo "App not running"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful!"
        }

        failure {
            echo "❌ Deployment Failed!"
        }
    }
}
