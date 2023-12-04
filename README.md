## Author 
[therohitthakur](https://github.com/therohitthakur)

# AI Model Deployment Pipeline

This project includes a simple AI model, a web service, and a deployment pipeline using Docker and Kubernetes.

## Table of Contents
1. [AI Model Development](#1-ai-model-development)
2. [Web Service Creation](#2-web-service-creation)
3. [Containerization with Docker](#3-containerization-with-docker)
4. [Deployment with Kubernetes](#4-deployment-with-kubernetes)

## 1. AI Model Development 
    The AI model is a text sentiment analysis model developed in Python using TensorFlow and Keras. It has been trained on a small dataset for simplicity. To run the model:
    
    ```bash
    python ai_model.py
## 2. Web-service-creation
    The web service is created using Flask in Python. It serves the AI model and exposes an API endpoint for predictions. To run the web service:**
    
    python web_service.py

## 3. Containerization-with-docker

    The AI model and web service can be containerized using Docker. Build the Docker image with:**
    
    ```bash
    
    docker build -t your-image-name .
    docker run -p 5000:5000 docker
## 4. Deployment-with-kubernetes
    Ensure you have a Kubernetes cluster set up. Deploy the application using the provided deployment.yaml:**
    
    kubectl apply -f deployment.yaml


