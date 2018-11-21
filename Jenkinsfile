pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
python3 manage.py test
python3 manage.py migrate
BUILD_ID=dontKillMe nohup python3 manage.py runserver & '''
      }
    }
  }
}