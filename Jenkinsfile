pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash
source /home/aditya/Courses/sem5/software_engineering_lab/project/django/bin/activate
python manage.py makemigrations








python manage.py migrate
python manage.py runserver'''
      }
    }
  }
}