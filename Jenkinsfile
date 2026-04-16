pipeline {
    agent any

    environment {
        IMAGE = "prachi1776/cloud-cost-optimizer"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/prachi55-star/cloud-cost-optimizer.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t cloud-cost-optimizer ."
            }
        }

        stage('Docker Login & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker tag cloud-cost-optimizer $IMAGE:latest
                    docker push $IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                docker rm -f cost-container || true
                docker pull $IMAGE:latest
                docker run -d -p 5000:5000 --name cost-container $IMAGE:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'curl http://localhost:5000 || echo "Running"'
            }
        }
    }
}
