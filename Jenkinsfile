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

        stage('List iamges') {
            steps {
                sh 'docker images'
            }
        }
    }
}