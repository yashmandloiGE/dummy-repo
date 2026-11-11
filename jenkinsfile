pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                // If running on Linux/macOS agent
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest pytest-playwright playwright
                playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution complete."
        }
    }
}