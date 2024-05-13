# Architecture

![Alt text](arch_diagram.png?raw=true "Data Pipeline")

## Data Pipeline Workflow

### Overview

The data pipeline workflow automates the process of training a machine learning model, saving artifacts, and building/pushing a Docker image to Azure Container Registry (ACR).

### Workflow Trigger
The workflow is triggered on push events to the `main` branch of the repository.

### Workflow Steps
1. **Checkout Code**
   - Action: `actions/checkout@v4`
   - Description: Fetches the code from the repository.

2. **Install Python**
   - Action: `actions/setup-python@v2`
   - Description: Sets up the Python environment for executing the pipeline steps.

3. **Install Dependencies**
   - Action: Custom script
   - Description: Installs Python dependencies specified in `requirements.txt`.

4. **Train Model and Save Artifacts**
   - Action: Custom script
   - Description: Trains the machine learning model and saves the trained model artifacts to a specific directory (`artifacts/`).

5. **Build and Push Docker Image**
   - Action: Custom script using Docker CLI
   - Description: Builds the Docker image for the ML Flask application and pushes it to Azure Container Registry (ACR).

6. **Upload Artifacts**
   - Action: `actions/upload-artifact@v3`
   - Description: Uploads the trained model artifacts to GitHub as an artifact named `trained-model-artifacts`.

## Deployment Pipeline Workflow

### Overview
The deployment pipeline workflow automates the deployment of the ML Flask application to Azure Kubernetes Service (AKS) after the data pipeline completes.

### Workflow Trigger
The workflow is triggered when the data pipeline workflow (`Data Pipeline`) completes successfully.

### Workflow Steps
1. **Checkout Code**
   - Action: `actions/checkout@v2`
   - Description: Fetches the code from the repository.

2. **Set up Azure CLI**
   - Action: `azure/login@v1`
   - Description: Sets up the Azure CLI using the Azure credentials stored in GitHub secrets.

3. **Azure AKS Set Context**
   - Action: Custom script using Azure CLI
   - Description: Sets the Azure Kubernetes Service (AKS) context for deployment.

4. **Deploy to AKS**
   - Action: Custom script using kubectl
   - Description: Deploys the ML Flask application to AKS using the Kubernetes manifest file (`deployment.yaml`).

### Additional Notes
- The deployment pipeline includes commented-out steps (`Download artifacts`, `Test artifacts Download`) that can be used for additional testing or validation if needed.
