pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Install dependencies
                sh 'pip3 install -r requirements.txt'
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
