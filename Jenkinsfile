pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/vijaysayyaparaju/selenium-ci-demo.git'

            }
        }

        stage('Install Selenium') {
            steps {
                bat 'python -m pip install selenium'
            }
        }

        stage('Run Selenium Test') {
            steps {
                bat 'python test_login.py'
            }
        }
    }

    post {
        always {
            echo 'Build completed!'
        }
        failure {
            echo 'Build failed ❌'
        }
        success {
            echo 'Build succeeded ✅'
        }
    }
}
