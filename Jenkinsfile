pipeline {
  agent any
  stages {
    stage('Stage') {
      steps {
        sh '''#!/bin/bash
docker-compose up --build -d'''
      }
    }
  }
}