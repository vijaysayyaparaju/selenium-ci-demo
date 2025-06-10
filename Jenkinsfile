pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest --html=reports/report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html, reports/*.png', allowEmptyArchive: true
        }
    }
}
