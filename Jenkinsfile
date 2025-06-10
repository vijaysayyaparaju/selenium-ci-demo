pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/vijaysayyaparaju/selenium-ci-demo.git'
            }
        }

        stage('Install Selenium') {
            steps {
                sh 'python -m pip install selenium'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh 'python test_login.py'
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
