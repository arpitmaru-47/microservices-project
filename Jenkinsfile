pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "appi47"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build frontend image') {
            steps {
                sh 'docker build -t appi47/frontend:v1 ./frontend'
            }
        }

        stage('Build backend image') {
            steps {
                sh 'docker build -t appi47/backend:v1 ./backend'
            }
        }

        stage('Docker login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push frontend image') {
            steps {
                sh 'docker push appi47/frontend:v1'
            }
        }

        stage('Push backend image') {
            steps {
                sh 'docker push appi47/backend:v1'
            }
        }
    }
}