pipeline {
    agent none
    stages {
        stage('Build & Deploy') {
            agent {
                docker {
                    image 'docker'
                }
            }
            steps {
                sh 'docker-compose build'
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}