pipeline {

    agent none

    stages {

        stage('Build and Execute APP') {

            agent {
                dockerfile {
                    filename 'Dockerfile'
                    dir '.'
                    additionalBuildArgs '--tag apasoft/temperatures'
                    args '-p 9191:80'
                    label 'docker-node'
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
        }

        stage('Docker Cleanup') {

            agent {
                label 'docker-node'
            }

            steps {

                echo 'Cleaning up Docker resources directly on docker-node...'

                sh '''
                    echo "Removing application image..."
                    docker rmi apasoft/temperatures:latest || true

                    echo "Removing Maven image..."
                    docker rmi maven:3.9.9-eclipse-temurin-17-alpine || true

                    echo "Removing Python image..."
                    docker rmi python:3.10-slim || true

                    echo "Removing unused Docker images..."
                    docker image prune -a -f || true

                    echo "Current Docker images:"
                    docker images
                '''

                echo 'Docker cleanup completed.'
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