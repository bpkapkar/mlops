# Deployment Pipeline Documentation

## Overview

![Alt text](deploy.png?raw=true "Deployment Pipeline")

This deployment pipeline automates the deployment of a trained machine learning model into an Azure Kubernetes Service (AKS) cluster. It utilizes GitHub Actions triggered by new artifacts from a data pipeline.

## Prerequisites

1. Azure Container Registry (ACR) to store Docker images.
2. Azure Kubernetes Service (AKS) cluster.
3. GitHub repository with ML model code, Dockerfile, and Kubernetes YAML files.

## Pipeline Structure

1. **Checkout Code**: Retrieves code from GitHub repository.
2. **Download Artifacts**: Fetches artifacts (trained model, dependencies) from data pipeline.
3. **Build Docker Image**: Creates Docker image with model and dependencies.
4. **Push Docker Image**: Stores Docker image in Azure Container Registry.
5. **Azure Login**: Logs into Azure for deployment.
6. **Deploy to AKS**: Deploys Docker image to Azure Kubernetes Service.

## Pipeline Configuration

- Triggered automatically by completed data pipeline workflow.
- Utilizes GitHub Actions and Azure CLI for automation.

## Usage

1. Ensure repository contains necessary files:
   - Dockerfile.
   - Kubernetes YAML files.
2. Set up GitHub repository secrets:
   - ACR_USERNAME.
   - ACR_PASSWORD.
   - AZURE_CREDENTIALS.
3. Customize pipeline configuration in GitHub Actions workflow file (`main.yaml`).
4. Test pipeline by triggering data pipeline run.
5. Monitor GitHub Actions workflow for deployment status.

## Troubleshooting

- Refer to GitHub Actions logs and Azure CLI output for errors.
- Common issues: authentication failures, Docker build errors, Kubernetes config problems.

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Azure CLI Documentation](https://docs.microsoft.com/en-us/cli/azure)
- [Azure Kubernetes Service (AKS) Documentation](https://docs.microsoft.com/en-us/azure/aks)
- [Use GitHub Actions to connect to Azure](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure?tabs=azure-portal%2Cwindows)
