pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // venv
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                // Install dependencies
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Run tests
                sh 'pytest'
            }
        }
    }

    post {
        always {
            // Archive test results, logs, etc.
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
            junit 'reports/**/*.xml'
        }
    }
}
