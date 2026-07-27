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
                sh 'docker build -t appi47/frontend:${BUILD_NUMBER} ./frontend'
            }
        }

        stage('Build backend image') {
            steps {
                sh 'docker build -t appi47/backend:${BUILD_NUMBER} ./backend'
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
                sh 'docker push appi47/frontend:${BUILD_NUMBER}'
            }
        }

        stage('Push backend image') {
            steps {
                sh 'docker push appi47/backend:${BUILD_NUMBER}'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                '''
            }
        }
    }
}