pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ajayrahangdale/devops-flask-app.git', credentialsId: 'dba8673b-7100-44fd-84cf-6a68e99c2560'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-devops-app:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'ajayrahangdale', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $ajayrahangdale --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker tag flask-devops-app:latest ajayrahangdale/flask-devops-app:latest'
                sh 'docker push ajayrahangdale/flask-devops-app:latest'
            }
        }
    }
}
