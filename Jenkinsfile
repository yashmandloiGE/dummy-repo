pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                // Runs pytest and generates both a log file and a standalone HTML report
                bat 'pytest --log-file=pytest.log --html=report.html --self-contained-html'
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution complete. Archiving logs and reports..."
            
            // Archives the generated pytest log and HTML report as build artifacts
            archiveArtifacts artifacts: 'pytest.log, report.html', allowEmptyArchive: true
        }
    }
}