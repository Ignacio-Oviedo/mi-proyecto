pipeline {
    agent {
        docker {
            image 'docker'
        }
    }
    stages {
        stage('Build & Deploy') {
            steps {
                sh 'docker-compose build'
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}