pipeline {
    agent any

    // 1. הגדרת זמן ריצה מקסימלי (שיניתי ל-30 שניות כדי שהריצה לא תיקטע סתם)
    options {
        timeout(time: 20, unit: 'SECONDS')
    }
    environment {
        APP_ENV = "build APP_ENV_try"
        MY_SECRET = credentials('my password')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                echo "Current Env: ${env.APP_ENV}"
                // הדפסת שם המשתמש מה-Credentials
                echo "Username: ${env.MY_SECRET_USR}"
                bat 'python build/build_script.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                bat 'set PYTHONPATH=. && python test/test_script.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                bat 'python deploy/deploy_script.py'
            }
        }
    }

    // בלוק סיום תמיד ידפיס הודעה בסוף הריצה
    post {
        always {
            echo 'Finished Pipeline execution.'
        }
    }
}