pipeline {
    agent any

    environment {
        APP_NAME = "Cloud Cost Optimizer"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning latest code from GitHub..."
                checkout scm
            }
        }

        stage('Verify Files') {
            steps {
                sh '''
                    echo "Current directory:"
                    pwd

                    echo "Files in workspace:"
                    ls -la
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies..."
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Stop Old Application') {
            steps {
                sh '''
                    echo "Stopping old Flask app..."
                    pkill -f app.py || true
                '''
            }
        }

        stage('Start Application') {
            steps {
                sh '''
                    echo "Starting Flask app..."

                    nohup python3 app.py > app.log 2>&1 &

                    sleep 5
                '''
            }
        }

        stage('Check Logs') {
            steps {
                sh '''
                    echo "Checking logs..."
                    cat app.log || echo "No logs found"
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Checking if app is running..."

                    ps -ef | grep app.py | grep -v grep || echo "App not running"

                    echo "Checking port 5000..."
                    sudo ss -tulnp | grep 5000 || echo "Port not active"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Application deployed successfully!"
        }
        failure {
            echo "❌ FAILED: Check logs in console output"
        }
    }
}
