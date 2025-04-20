pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Functional Tests') {
            steps {
                sh 'pytest src/tests/functional'
            }
        }
        stage('Run Integration Tests') {
            steps {
                sh 'pytest src/tests/integration'
            }
        }
        stage('Build') {
            steps {
                echo 'Build stage: Preparing for deployment...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy stage: Application deployed!'
            }
        }
    }
}