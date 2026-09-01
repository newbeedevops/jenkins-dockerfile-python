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
            echo 'Pipeline completed.'
        }

        success {
            echo 'Pipeline executed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}