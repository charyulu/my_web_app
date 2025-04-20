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
                echo 'Building the application...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}