pipeline {
  agent any
  options {
      buildDiscarder(logRotator(numToKeepStr: '10',
                                daysToKeepStr: '5',
                                artifactNumToKeepStr: '10',
                                artifactDaysToKeepStr: '5'))
  }
  environment {
    IMAGE_NAME              = "us.gcr.io/jenkins-ci-cd-278717/itshop"
  }
  stages {
    stage('Build') {
      steps {
        sh "docker build -f docker/Dockerfile -t $IMAGE_NAME ."
      }
    }
    stage('Unit Test') {
	  agent { docker { image "$IMAGE_NAME" } }
      steps {
        sh "python -m unittest discover tests -p '*_test.py'"
      }
    }
    stage('Deploy') {
      steps {
        sh "scp -r * shop.vkr.sidorov.space:~/app"
      }
    }
  }
}
