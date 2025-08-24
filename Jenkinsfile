pipeline {
    agent {
        docker {
            image 'docker'
        }
    }
    stages {
        stage('Build & Deploy') {
            steps {
		sh 'chmod 666 /var/run/docker.sock'
                sh 'docker-compose build'
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}