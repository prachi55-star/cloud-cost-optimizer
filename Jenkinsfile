pipeline {
    agent any

    environment {
        APP_DIR = "cloud-cost-optimizer"
    }

        stage('Verify Files') {
            steps {
                sh '''
                    echo "Current directory:"
                    pwd

                    echo "Listing files:"
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

                    # go into folder
                    cd cloud-cost-optimizer || exit 1

                    # start app in background
                    nohup python3 app.py > app.log 2>&1 &

                    sleep 5
                '''
            }
        }

        stage('Check Logs') {
            steps {
                sh '''
                    echo "Checking application logs..."
                    cd cloud-cost-optimizer

                    cat app.log || echo "No log file found"
                '''
            }
        }

        stage('Verify Running App') {
            steps {
                sh '''
                    echo "Checking if app is running..."

                    ps -ef | grep app.py | grep -v grep || echo "App not running"

                    sudo ss -tulnp | grep 5000 || echo "Port 5000 not open"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment SUCCESS - App should be running!"
        }

        failure {
            echo "❌ Deployment FAILED - check logs"
        }
    }
}
