pipeline {
  agent any
  stages {
    stage('Install Docker') {
      steps {
        sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
        sh 'sh get-docker.sh'
        sh 'curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose'
        sh 'chmod +x /usr/local/bin/docker-compose'
      }
    }
    stage('Build & Deploy') {
      steps {
        sh 'docker-compose build'
        sh 'docker-compose down'
        sh 'docker-compose up -d'
      }
    }
  }
}