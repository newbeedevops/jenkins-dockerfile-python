pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir '.'
            additionalBuildArgs '--tag apasoft/temperatures'
            args '-p 9191:80'
        }
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building the Docker image..'
                // Jenkins builds the Docker image using the Dockerfile
            }
        }

        stage('Execute APP') {
            steps {
                withCredentials([
                    string(
                        credentialsId: 'openweather-api-key',
                        variable: 'OPENWEATHER_API_KEY'
                    )
                ]) {
                    sh '''
                        echo "Running temperature application..."
                        python /app/temperature.py
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Cleaning up Docker resources...'
    
            // Remove explicitly tagged application image
            sh 'docker rmi apasoft/temperatures:latest || true'
    
            // Remove tool/runtime images used by the pipeline
            sh 'docker rmi maven:3.9.9-eclipse-temurin-17-alpine || true'
            sh 'docker rmi python:3.10-slim || true'
    
            // Remove dangling/intermediate images created during Docker builds
            sh 'docker image prune -f || true'
    
            echo 'Docker cleanup completed.'
        }
    
        success {
            echo 'Pipeline executed successfully.'
        }
    
        failure {
            echo 'Pipeline failed.'
        }
    }
    
}