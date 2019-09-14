pipeline {
  agent {
    docker {
      image 'python:alpine'
      args '--rm'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'ls *'
        sh 'pip install -r requirements.txt'
        sh 'python app.py &'
      }
    }
    stage('test') {
      steps {
        sh '''python testHttp.py
'''
      }
    }
    stage('deploy') {
      steps {
        sh 'echo "It will be deployed as docker-compose and on kubernetes !"'
      }
    }
  }
}