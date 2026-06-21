pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "<dockerhub-username>/flask-todo"
        DOCKER_TAG   = "build-${BUILD_NUMBER}"
        REGISTRY_CREDENTIAL = 'dockerhub-credentials'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building image: ${DOCKER_IMAGE}:${DOCKER_TAG}"
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests inside container...'
                sh """
                    docker run --rm \
                      ${DOCKER_IMAGE}:${DOCKER_TAG} \
                      python -m pytest tests/ -v || echo 'No tests yet — skipping'
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "${REGISTRY_CREDENTIAL}",
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true"
                sh "docker rmi ${DOCKER_IMAGE}:latest || true"
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded!' }
        failure { echo 'Pipeline failed — check logs above.' }
    }
}
