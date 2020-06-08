pipeline {
  agent any
  options {
      buildDiscarder(logRotator(numToKeepStr: '10',
                                daysToKeepStr: '5',
                                artifactNumToKeepStr: '10',
                                artifactDaysToKeepStr: '5'))
  }
  environment {
    COMMIT_HASH = """${sh(
                   returnStdout: true,
                   script: 'git rev-parse --short=12 HEAD'
                   ).trim()}"""
    PROJECT_NAME            = "jenkins-ci-cd-278717"
    IMAGE_NAME              = "${PROJECT_NAME}/itshop"
    CONTAINER_REGISTRY      = "us.gcr.io"
  }
  stages {
    stage('Build') {
      steps {
        script {
          docker.build("${env.IMAGE_NAME}", "-f ./docker/Dockerfile .")
        }
      }
    }
    stage('Unit Test') {
	  agent { docker { image "$IMAGE_NAME" } }
      steps {
        sh "python -m unittest discover tests -p '*_test.py'"
      }
    }
    stage('Delivery') {
      steps {
        script {
          dockerImage = docker.image("${env.IMAGE_NAME}")
          docker.withRegistry("https://${env.CONTAINER_REGISTRY}", "gcr:jenkins-ci-cd-278717") {
            dockerImage.push("${env.COMMIT_HASH}")
            dockerImage.push("latest")
          }
        }
      }
    }
  }
}
