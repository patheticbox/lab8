pipeline {
    agent any

    triggers {
        // Poll SCM: перевірка змін у репозиторії кожні 5 хвилин
        pollSCM('H/5 * * * *')
    }

    environment {
        HEADLESS = 'true'
        PATH = "${env.HOME}/.local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/patheticbox/lab8.git'
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh 'python3 -m pip install --user --break-system-packages pylint'
                sh 'python3 -m pylint --disable=C,R,E0401 features pages'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user --break-system-packages -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    sh 'python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure-results -f pretty'
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
