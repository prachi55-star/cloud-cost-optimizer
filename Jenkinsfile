pipeline {
    agent any

    environment {
        IMAGE_NAME = "cost-optimizer"
        CONTAINER_NAME = "cost-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning latest code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker image..."
                    docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    echo "Stopping old container..."
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                    echo "Starting new container..."
                    docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Checking running containers..."
                    docker ps

                    echo "Checking app..."
                    sleep 5
                '''
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Docker Deployment Completed!"
        }
        failure {
            echo "❌ FAILED: Check Jenkins logs"
        }
    }
}
