pipeline {
    agent any
    enviroment{
    APP_ENV="build APP_ENV"
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                echo '${APP_ENV}'
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