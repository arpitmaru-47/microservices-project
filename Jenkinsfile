pipeline {
    agent any

    stages {

        stage('Clone Verification') {
            steps {
                sh 'pwd'
                sh 'ls -ls'
            }
        }

        stage('Git Check') {
            steps {
                sh 'git --version'
            }
        }

        stage('Docker Check'){
            steps {
                sh 'docker --vesion'
                sh 'docker images'
            }
        }
    }
}