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

    SSH_KEY_ID              = "my3uk_ssh_key"
    WEB_SERVER_NAME         = "django-shop-1"
    WEB_SERVER_HOST         = "shop.vkr.sidorov.space"
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
    stage('Web Server Pulling') {
      steps {
        script {
          remote = [:]
          remote.name = "${env.WEB_SERVER_NAME}"
          remote.host = "${env.WEB_SERVER_HOST}"
          remote.allowAnyHosts = true

          withCredentials([sshUserPrivateKey(credentialsId: "${env.SSH_KEY_ID}", keyFileVariable: 'identity',
                                             passphraseVariable: '', usernameVariable: 'userName')]) {
            remote.user = userName
            remote.identityFile = identity
            sshCommand remote: remote, command: 'cd app && docker-compose pull'
          }
        }
      }
    }
  }
}
