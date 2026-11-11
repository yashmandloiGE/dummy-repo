pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                // Use 'bat' for Windows agents instead of 'sh'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install pytest pytest-playwright playwright
                playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
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