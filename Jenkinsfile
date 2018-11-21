pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
source /home/aditya/Courses/sem5/software_engineering_lab/project/django/bin/activate
pip install -r --user requirements.txt
python manage.py test
python manage.py migrate
BUILD_ID=dontKillMe nohup python manage.py runserver & '''
      }
    }
  }
}