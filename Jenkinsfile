pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker version') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build frontend image') {
            steps {
                sh 'docker build -t frontend:v1 ./frontend'
            }
        }

        stage('Build backend image') {
            steps {
                sh 'docker build -t backend:v1 ./backend'
            }
        }

        stage('List iamges') {
            steps {
                sh 'docker images'
            }
        }
    }
}