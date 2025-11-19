pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "your_dockerhub_ajayrahangdale"
        IMAGE_NAME = "flask-devops-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ajayrahangdale/devops-flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKERHUB_ajayrahangdale/$IMAGE_NAME:latest .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_TOKEN | docker login -u $DOCKERHUB_ajayrahangdale --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push $ajayrahangdale/$IMAGE_NAME:latest'
                }
            }
        }
    }
}
