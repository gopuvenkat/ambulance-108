pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
python3 manage.py migrate
python3 manage.py test
BUILD_ID=dontKillMe nohup python3 manage.py runserver & '''
      }
    }
  }
}