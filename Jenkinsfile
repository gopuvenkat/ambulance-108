pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
pip install -r requirements.txt
source /home/aditya/Courses/sem5/software_engineering_lab/project/django/bin/activate
python manage.py makemigrations
python manage.py migrate
BUILD_ID=dontKillMe nohup python manage.py runserver & '''
      }
    }
  }
}