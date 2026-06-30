pipeline {
    agent any

    environment {
        DOCKER_IMAGE          = "themxnish/flask-todo"
        DOCKER_TAG            = "build-${BUILD_NUMBER}"
        REGISTRY_CREDENTIAL   = 'dockerhub-credentials'
        SONAR_TOKEN           = credentials('sonar-token')
        KUBE_DEPLOYMENT       = 'flask-todo-deployment'
        KUBE_CONTAINER        = 'flask-todo'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh """
                    /opt/sonar-scanner/bin/sonar-scanner \
                      -Dsonar.projectKey=flask-todo \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://192.168.172.129:9000 \
                      -Dsonar.token=${SONAR_TOKEN}
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    docker run --rm \
                      ${DOCKER_IMAGE}:${DOCKER_TAG} \
                      python -m pytest test/ -v
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

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                    kubectl set image deployment/${KUBE_DEPLOYMENT} \
                      ${KUBE_CONTAINER}=${DOCKER_IMAGE}:${DOCKER_TAG} \
                      --record

                    kubectl rollout status deployment/${KUBE_DEPLOYMENT} \
                      --timeout=120s
                """
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true"
            }
        }
    }

    post {
        success { echo "Deployed ${DOCKER_IMAGE}:${DOCKER_TAG} to Kubernetes." }
        failure { echo 'Pipeline failed. Rolling back...'
                  sh 'kubectl rollout undo deployment/${KUBE_DEPLOYMENT} || true' }
    }
}
