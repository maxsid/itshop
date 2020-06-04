pipeline {
  agent any
  options {
      buildDiscarder(logRotator(numToKeepStr: '10',
                                daysToKeepStr: '5',
                                artifactNumToKeepStr: '10',
                                artifactDaysToKeepStr: '5'))
  }
  stages {
    stage('Test') {
      steps {
        sh "python3 -m unittest"
      }
    }
    stage('Deploy') {
      steps {
        sh "scp -r * shop.vkr.sidorov.space:~/app"
      }
    }
  }
}
