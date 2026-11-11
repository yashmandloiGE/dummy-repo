pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                // Runs pytest directly using the system Python environment on Windows
                bat 'pytest'
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution complete."
        }
    }
}