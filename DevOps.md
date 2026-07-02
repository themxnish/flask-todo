# DevOps Practice - Flask Todo Application

> **Note:** This repository is a **fork** of a simple Flask Todo application. The application itself was not developed by me. This fork was created solely for practicing DevOps concepts and implementing a complete CI/CD workflow using industry-standard tools.

---

# Practice Overview

The objective of this repository is to demonstrate how a basic Python Flask application can be transformed into a production-ready application using modern DevOps practices.
Instead of focusing on application development, this project focuses on the software delivery lifecycle - from source code management to automated deployment on my personal virtual machine.

During this practice, I successfully integrated multiple DevOps tools and technologies including:

- Git & GitHub
- Docker
- Jenkins
- SonarQube
- Kubernetes
- Monitoring
- Ubuntu virtual machine

This repository documents my learning practice to understand how these tools work together.

---

# Objectives

The primary goals of this practice were to:

- Understand Git workflows using a forked repository by branching
- Learn Docker image creation, composing images and containerization
- Configure complete Jenkins pipelines for CI/CD automation and Auto-trigger on Push
- Integrate SonarQube pytest unit tests for static code analysis
- Deploy containerized applications on Kubernetes (minikube)
- Understand how each DevOps tool fits into a real development pipeline on a production grade server

---

# Technologies Used

| Tool | Purpose |
|------|---------|
| Git | Version control |
| GitHub | Source code hosting |
| Flask | Sample Python web application |
| Docker | Containerization |
| Jenkins | Continuous Integration / Continuous Deployment |
| SonarQube | Code Quality & Static Analysis |
| Kubernetes | Container Orchestration |
| Minikube |	Local Kubernetes Cluster |
| Ubuntu VM |	Development Environment |

---

# DevOps Workflow

The following workflow was implemented during this practice:

```text
Developer
     │
     ▼
 Git Commit
     │
     ▼
 GitHub Repository
     │
     ▼
 Jenkins Pipeline
     │
     ├──────────────► Checkout Source
     │
     ├──────────────► Install Dependencies
     │
     ├──────────────► Run Tests
     │
     ├──────────────► SonarQube Analysis
     │
     ├──────────────► Build Docker Image
     │
     ├──────────────► Push Image 
     │
     ▼
 Kubernetes Deployment
     │
     ▼
 Running Flask Application
```

---

# Project Structure

```
.
├── app.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── configmap.yaml
└── test/
```

# Implementation

## Step 1 – Clone Repository & Run Application

Clone the forked repository, create a Python virtual environment, install project dependencies, and verify that the Flask application runs successfully on the local Ubuntu VM.

```bash
# Clone repository
git clone https://github.com/themxnish/flask-todo
cd flask-todo

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

---

## Step 2 – Docker Containerization

Build a Docker image from the application source and run it as a container to ensure a consistent and portable runtime environment.

```bash
# Build Docker image
docker build -t flask-todo:v1 .

# Run Docker container
docker run -d \
  --name flask-todo \
  -p 5000:5000 \
  flask-todo:v1

# Verify running container
docker ps
```

---

## Step 3 – Static Code Analysis with SonarQube

Analyze the source code using SonarQube to identify bugs, vulnerabilities, code smells, and maintainability issues before deployment.

```bash
# Execute SonarQube scan
sonar-scanner
```

---

## Step 4 – Continuous Integration with Jenkins

Configure a Jenkins pipeline to automate source code checkout, dependency installation, testing, SonarQube analysis, Docker image creation, and deployment preparation.

```bash
# Jenkins automatically executes the pipeline
# Typical pipeline stages:
Checkout → Install Dependencies → Tests → SonarQube Scan → Docker Build → Deploy
```

---

## Step 5 – Kubernetes Deployment

Deploy the Dockerized application to a Kubernetes cluster using Deployment, Service, and ConfigMap manifests, then verify that all resources are running successfully.

```bash
# Deploy Kubernetes resources
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify deployment
kubectl get pods
kubectl get services
kubectl get deployments
```

# Conclusion

This repository represents a practical DevOps learning project that demonstrates how a simple Flask application can progress through a modern software delivery pipeline. It showcases the integration of Git, Docker, Jenkins, SonarQube, and Kubernetes to automate building, testing, analyzing, and deploying an application.