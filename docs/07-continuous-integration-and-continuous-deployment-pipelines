# 7. Continuous Integration and Continuous Deployment (CI/CD) Pipelines

## 7.1 Overview
In this section, I will describe how I set up CI/CD pipelines for the My Demo App using Red Hat OpenShift Pipelines (Tekton). These pipelines automate the process of building, testing, and deploying the application. The CI/CD process helps ensure that the application is built, tested, and deployed consistently and reliably across different environments.

---

## 7.2 Pipelines Setup

### 7.2.1 Tekton Pipeline Files

The CI/CD process is managed using Tekton pipelines. The following files have been created and placed in the `pipelines/` directory of the project:

- **`git-clone.yaml`**: This task is responsible for cloning the source code from the GitHub repository.
- **`build-app.yaml`**: This task builds the container images for the backend and frontend services.
- **`run-tests.yaml`**: This task runs the backend and frontend tests to ensure the application is functioning correctly.
- **`deploy-app.yaml`**: This task handles the deployment of the backend and frontend services to the OpenShift cluster.

### 7.2.2 Pipeline Definitions

The pipelines are defined in the following files located in the `pipelines/` directory:

- **`pipeline.yaml`**: This file defines the sequence of tasks that will be executed as part of the CI/CD pipeline.
- **`pipeline-run.yaml`**: This file is used to trigger the pipeline run and provide the necessary parameters such as Git URL, image URL, and workspace information.

---

## 7.3 Deployment Manifests

### 7.3.1 Deployment Files

Deployment manifests have been created and placed in the `manifests/` directory. These files define how the backend and frontend services are deployed in the OpenShift environment.

- **`backend-deployment.yaml`**: This file defines the deployment configuration for the backend service, including the number of replicas, container specifications, environment variables, and resource requirements.
- **`frontend-deployment.yaml`**: This file defines the deployment configuration for the frontend service.
- **`db-deployment.yaml`**: This file defines the deployment configuration for the PostgreSQL database.
- **`service.yaml`**: This file defines the services that expose the backend and frontend applications to external traffic.
- **`ingress.yaml`**: This file defines the ingress rules for routing external traffic to the appropriate services.

---

## 7.4 Project Structure Update

The project structure has been updated to reflect the new directories and files created for CI/CD pipelines and deployment manifests.

```plaintext
my-demo-app/
├── docs/                        # Documentation files
├── src/                         # Source code for the application
│   ├── backend/                 # Backend code (Flask application)
│   │   ├── app.py               # Main application entry point
│   │   ├── config.py            # Configuration settings for the application
│   │   ├── extensions.py        # Extensions like SQLAlchemy
│   │   ├── models.py            # Database models
│   │   ├── requirements.txt     # Python dependencies
│   │   ├── migrations/          # Database migration files
│   │   ├── __tests__/           # Backend tests
│   ├── frontend/                # Frontend code (HTML, CSS, JavaScript)
│   │   ├── templates/           # HTML templates
│   │   ├── static/              # Static files (CSS, JS, images)
│   │   ├── cypress/             # Cypress end-to-end tests
├── pipelines/                   # Tekton pipeline files
│   ├── git-clone.yaml           # Pipeline task for cloning the GitHub repository
│   ├── build-app.yaml           # Pipeline task for building container images
│   ├── run-tests.yaml           # Pipeline task for running tests
│   ├── deploy-app.yaml          # Pipeline task for deploying the application
│   ├── pipeline.yaml            # Main pipeline definition
│   ├── pipeline-run.yaml        # Pipeline run configuration
├── manifests/                   # Kubernetes/OpenShift deployment manifests
│   ├── backend-deployment.yaml  # Deployment configuration for the backend
│   ├── frontend-deployment.yaml # Deployment configuration for the frontend
│   ├── db-deployment.yaml       # Deployment configuration for the PostgreSQL database
│   ├── service.yaml             # Service definitions for backend and frontend
│   ├── ingress.yaml             # Ingress configuration for routing traffic
├── .gitignore                   # Files and directories to be excluded from version control
├── Dockerfile                   # Dockerfile for containerising the application
└── README.md                    # Project overview and setup instructions
```

## 7.5 Troubleshooting and Future Steps

### 7.5.1 Current Issues

- **Build Failures**: Issues with UID mapping and file permissions during the build process.
- **Deployment Errors**: Deployment failures due to missing configurations or incorrect setup.
- **Pipeline Execution**: Need to resolve issues with pipeline execution, including workspace setup and resource configurations.

### 7.5.2 Next Steps

- **Remediation**: Focus on troubleshooting and resolving the current issues.
- **Security Enhancements**: Continue working on securing environment variables and credentials.
- **Production Readiness**: Prepare the application for deployment to the production environment.