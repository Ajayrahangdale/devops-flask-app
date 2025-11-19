pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "your_dockerhub_username"
        DOCKERHUB_TOKEN = credentials('dockerhub-token')
        IMAGE_NAME = "flask-devops-app"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh "echo $DOCKERHUB_TOKEN | docker login -u $DOCKERHUB_USERNAME --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:latest'
            }
        }
    }
}
