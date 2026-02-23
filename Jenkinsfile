pipeline {
    agent any
     options {
        timeout(time: 10, unit: 'SECONDS')
        buildDiscarder(logRotator(numToKeepStr: '4'))

    }
    environment{
    APP_ENV="build APP_ENV_try"
    }
    stages {
    stage('learn credentials') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: '123',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )
            ]) {
                bat '''
                    echo Deploying as %USER% %PASS%
                '''
            }
        }
    }
        stage('Build') {
            steps {
                echo 'Building...'
                echo  "${APP_ENV}"
                bat 'python build/build_script.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                bat 'python test/test_script.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                bat 'python deploy/deploy_script.py'
            }
        }
    }
}