pipeline {
    agent any

    // הגדרת זמן ריצה מקסימלי (Timeout) - ירוץ עד 30 שניות כדי שלא ייכשל סתם
    options {
        timeout(time: 30, unit: 'SECONDS')
    }

    environment {
        APP_ENV = "build APP_ENV_try"
        // משיכת שם המשתמש והסיסמה מה-ID שהגדרת בג'נקינס
        MY_SECRET = credentials('my password')
    }

    stages {
        stage('Build') {
            steps {
                echo "Building in ${env.APP_ENV}..."
                // הדפסת שם המשתמש מה-Credentials
                echo "Username: ${env.MY_SECRET_USR}"
                bat 'python build/build_script.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // פתרון שגיאת ה-src שראינו קודם
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

    post {
        always {
            echo 'Pipeline finished execution.'
        }
    }
}