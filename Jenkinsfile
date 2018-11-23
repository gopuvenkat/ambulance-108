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

if [ -e /tmp/ambulance.pid ]
then
    echo "Found pid file. Killing process..."
    kill -9 $(cat /tmp/ambulance.pid)
else
    echo "No previous process found."
fi

nohup python3 manage.py runserver &
echo $! > /tmp/ambulance.pid'''
      }
    }
  }
}