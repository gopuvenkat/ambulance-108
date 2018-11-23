pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
python3 manage.py migrate'''
      }
    }
    stage('Test') {
      steps {
        sh '''#!/bin/bash
python3 manage.py test
'''
      }
    }
    stage('Deploy') {
      steps {
        sh '''#!/bin/bash
BUILD_ID=dontKillMe nohup python3 manage.py runserver '''
      }
    }
  }
}