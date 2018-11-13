pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''python manage.py makemigrations




python manage.py migrate
python manage.py runserver'''
      }
    }
  }
}