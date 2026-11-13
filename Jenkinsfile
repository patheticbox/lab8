pipeline {
    agent any

    triggers {
        // Poll SCM: перевірка змін у репозиторії кожні 5 хвилин
        pollSCM('H/5 * * * *')
    }

    environment {
    HEADLESS = 'true'
    PY = 'C:\\Users\\Pathetic_Box\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    PYTHONUTF8 = '1'
    PATH = "C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\WindowsPowerShell\\v1.0;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/patheticbox/lab8.git'
            }
        }

        stage('Static Code Analysis') {
            steps {
                bat '"%PY%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install pylint'
                bat 'venv\\Scripts\\python -m pylint --disable=C,R,E0401 features pages'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat 'venv\\Scripts\\python -m behave -f allure_behave.formatter:AllureFormatter -o allure-results -f pretty'
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
