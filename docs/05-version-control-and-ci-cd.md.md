# 5. Version Control and CI/CD
In this section, I’ll outline the version control practices I’m using for the My Demo App project and provide an introduction to Continuous Integration (CI) using Tekton. This will also lay the groundwork for future Continuous Deployment (CD) processes, which I plan to implement as I progress to an OpenShift environment.

## 5.1 Version Control with Git

### 5.1.1 Repository Structure
The project is version-controlled using Git and hosted on GitHub. Here’s how I’ve organised the repository:

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
│   │   ├── database/            # Database-related scripts or files
│   ├── frontend/                # Frontend code (HTML, CSS, JavaScript)
│   │   ├── templates/           # HTML templates
│   │   ├── static/              # Static files (CSS, JS, images)
├── .gitignore                   # Files and directories to be excluded from version control
├── Dockerfile                   # Dockerfile for containerising the application
└── README.md                    # Project overview and setup instructions
```

### 5.1.2 Git Practices Used

To keep the codebase clean and manageable, I’m following these Git best practices:

- **Commit Frequently**: Commit changes often with clear and descriptive messages.
- **Branching Strategy**: Use feature branches for new features, bug fixes, or experiments. Merge into the main branch via pull requests.
- **Code Reviews**: All changes should be reviewed before being merged into the main branch.
- **Tagging Releases**: Use Git tags to mark specific releases or milestones in the project.

### 5.1.3 Setting up the Repository
To setup the repository

1. **Clone the Repository**:
```bash
git clone https://github.com/your-username/my-demo-app.git
cd my-demo-app
```

2. **Check Out a New Branch**:
```bash
git checkout -b feature/your-feature-name
```

3. **Add and Commit Changes**:
```bash
git add .
git commit -m "Description of your changes"
```

4. **Push Changes to GitHub**:
```bash
git push origin feature/your-feature-name
```

### 5.1.4 Versioning and Environment Variables

To manage different versions and environments of the My Demo App, I’ve introduced environment variables and version tags within the codebase:

- **Versioning**: The application version is stored as an environment variable `APP_VERSION`. This allows for tracking which version of the app is running in different environments. This is essential for maintaining consistency and traceability across different stages of development and deployment.
- **Environment Specification**: The `APP_ENV` environment variable is used to specify the environment (development, staging, production). This helps ensure that development versions are not accidentally deployed to production.

__Example Code Integration__:

In `app.py`, these variables are integrated as follows:

```python
class Config:
    VERSION = "0.1.0-dev"
    ENVIRONMENT = os.getenv('APP_ENV', 'development')

# In the application setup:
if Config.ENVIRONMENT == 'development':
    print("Warning: You are running a development version of the application (Version: {Config.VERSION}).")
    if os.getenv('ALLOW_DEPLOY_TO_NON_PROD') != 'true':
        sys.exit("Error: Deployment of development version to non-prod/prod is not allowed.")
elif Config.ENVIRONMENT == 'production':
    print(f"Running in production mode (Version: {Config.VERSION}).")
```

### 5.1.5 Podman and Compose Configuration

The integration of environment variables and versioning is also reflected in the docker-compose.yml setup. This ensures that the application is consistently deployed across different environments with the correct version information.

You can review the docker-compose file in the projects `root` folder

This configuration ensures that the appropriate environment and version information are passed to the containers at runtime, providing a seamless and consistent setup across development and deployment environments.

## 5.2 Preparing for Continuous Integration with OpenShift Pipelines

### 5.2.1 Introduction to OpenShift Pipelines

OpenShift Pipelines, based on Tekton, is a Kubernetes-native CI/CD solution that I’ll be using to automate the build and test processes for My Demo App. While I haven’t deployed to an OpenShift environment yet, setting up these pipelines now will lay a solid foundation for future CI/CD implementations. OpenShift Pipelines provides a consistent and scalable approach to automating various stages of the software development lifecycle, from code integration to deployment. This setup will ensure that the application is ready for seamless deployment in an OpenShift environment as the project progresses.

### 5.2.2 Initial Setup on a Local Environment

Since I’m currently working on a local environment (such as a spare laptop running Single Node OpenShift (SNO)), I can begin experimenting with OpenShift Pipelines by setting up a minimal pipeline:

- **Install OpenShift Pipelines**: I need to ensure that OpenShift Pipelines (based on Tekton) are installed on my local OpenShift or Kubernetes cluster.
- **Create Basic Tekton Tasks**: I’ll start with simple tasks, such as checking out the code from GitHub and running basic tests.

### 5.2.3 Expanding CI with OpenShift Pipelines

Once I transition to a more robust environment like ROSA, I plan to expand my Tekton pipelines to include more complex tasks, such as:

   - **Building Docker Images**: Automating the build process for my Docker images.
   - **Running Tests**: Integrating my testing framework into the pipeline to ensure code quality.

### 5.2.4 Building and Pushing Images to Quay.io

Before triggering the pipeline for the first time, it’s essential to ensure that your application images are available in a container registry like Quay.io. This is a crucial step in the CI process because the pipeline relies on these pre-built images for testing, deployment, and further automation.

In this section, I’ll outline the step-by-step process to build and push the backend and frontend images of My Demo App to Quay.io. Completing these steps ensures that the pipeline has the necessary images available to pull and deploy the application seamlessly.

__Steps to Build and Push Images__

1.	**Login to Quay.io**:
Use the podman login command to authenticate with your Quay.io account.
```bash
podman login quay.io
```

2. **Build the Backend Image**:
Navigate to the src/backend/ directory and build the backend image with the appropriate version tag.
```bash
podman build -t quay.io/your-quay-username/my-demo-app-backend:v0.2.0-dev .
```

3. **Push the Backend Image**:
Push the built image to Quay.io.
```bash
podman push quay.io/your-quay-username/my-demo-app-backend:v0.2.0-dev
```

4. **Build the Frontend Image**:
Navigate to the src/frontend/ directory and build the frontend image.
```bash
podman build -t quay.io/your-quay-username/my-demo-app-frontend:v0.2.0-dev .
```

5. **Push the Frontend Image:
Push the frontend image to Quay.io.
```bash
podman push quay.io/your-quay-username/my-demo-app-frontend:v0.2.0-dev
```

By following these steps, you ensure that your backend and frontend images are available in Quay.io for use in your OpenShift pipelines and deployments. This setup is necessary for the successful execution of the CI/CD pipeline, allowing the application to be built, tested, and deployed efficiently.

## 5.3 Configuring Secrets for Image Pulls

When working with private container registries like Quay.io, it’s essential to secure your image pulls to ensure that only authorized users and systems can access your images. This step is crucial in maintaining the security and integrity of your CI/CD pipeline, especially when deploying sensitive or production-grade applications.

In this section, I’ll walk through the process of creating and configuring the necessary secrets in OpenShift to enable secure image pulls from Quay.io. These steps are necessary to ensure that your deployments can access the required container images without any unauthorized access issues.

### 5.3.1 Creating the Secret for Quay.io

1. **Generate a Quay.io Access Token:**
   - Navigate to your [Quay.io account settings](https://quay.io/user/) and generate a new access token.
   
2. **Create the Secret:**
   - Use the following command to create a secret in your OpenShift project:
     ```bash
     oc create secret docker-registry quay-secret \
       --docker-server=quay.io \
       --docker-username=<quay-username> \
       --docker-password=<quay-access-token> \
       --docker-email=<your-email> \
       -n my-demo-app
     ```

3. **Link the Secret to the Service Account:**
   - Link the secret to the `default` service account to allow image pulls:
     ```bash
     oc secrets link default quay-secret --for=pull -n my-demo-app
     ```

### 5.3.2 Verifying Secret Configuration

After creating and linking the secret, verify that it's correctly associated with your service account:

```bash
oc get serviceaccount default -o yaml -n my-demo-app
```

Ensure that the output includes your `quay-secret` under the `imagePullSecrets` section, like this:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: default
  namespace: my-demo-app
secrets:
- name: quay-secret
imagePullSecrets:
- name: quay-secret
```

If the secret is listed under imagePullSecrets, your service account is correctly configured to pull images from Quay.io.

### 5.3.3 Troubleshooting

If you encounter issues with image pulls, check the following:

- **Secret Validity**: Ensure that the Quay.io access token is still valid.
- **Namespace**: Verify that the secret is created in the correct namespace (my-demo-app).
- **Service Account**: Confirm that the secret is correctly linked to the default service account in your project.

## 5.4 Future Considerations for Continuous Deployment

As the My Demo App project evolves, further enhancements to the CI/CD pipeline will be explored, particularly in the area of Continuous Deployment (CD). While this section outlines key considerations and strategies for CD, detailed steps will be addressed in later phases of the project. This approach ensures that foundational elements are solidified before expanding into more complex deployment scenarios, such as deploying to production environments or integrating advanced GitOps practices.

### 5.4.1 Planning for Deployment

When I’m ready to deploy my application to an OpenShift environment, I’ll expand my Tekton pipelines to include deployment tasks. This will likely involve:

   - **Deploying to OpenShift**: Using oc commands or Kubernetes manifests to deploy my application.
   - **Running Migrations**: Applying database migrations as part of the deployment proces

### 5.4.2 Incorporating GitOps with Argo CD

As I gain more experience with OpenShift, I’m considering integrating GitOps practices using Argo CD. This approach will allow me to manage deployments declaratively, with Git as the single source of truth.

## 5.5 Tagging and Prepartion for Deployment

Tagging plays a critical role in the CI/CD pipeline, serving as a way to mark specific points in the development process that are ready for deployment. By assigning version tags, we can ensure that the exact state of the code at a given time is preserved, making it easier to track changes, roll back if necessary, and maintain consistency across different environments. This section outlines the steps taken to properly tag the My Demo App and prepare it for deployment, reinforcing the importance of version control in a robust CI/CD pipeline.

### 5.5.1 Staging and Committing Changes

Before tagging the new version of the application, I ensured that all recent changes were staged and committed to the Git repository.

Steps:

1.	**Stage the Changes**: All modified files were added to the Git staging area using the following command:
```bash
git add .
```

2. **Commit the Changes**
```bash
git commit -m "<Insert relevant comment>"
```

### Taggin the Version

Once all changes were committed, I proceeded to tag the version. This version tag marks the point in the codebase where environment variables were introduced, and database credentials were secured.

__Steps__:

1.	**Create a Version Tag**:
The following command was used to create an annotated tag for version 0.2.0-dev:
```bash
git tag -a v<Enter Version, e.g. 0.2.0>-dev -m "V<Enter valid comment, e.g. Version 0.2.0-dev: Introduced environment variables and secured database credentials.>"
```

2. **Push the Tag to GitHub**:
To ensure the version tag is available in the remote repository, I pushed the tag along with the latest commits using:
```bash
git push origin main --tags
```

This process ensures that all updates are clearly marked and traceable in the project’s history, facilitating better management of the application’s lifecycle.

### 5.6 Versioning Strategy

Maintaining a consistent versioning strategy is essential for managing the lifecycle of an application, especially in a CI/CD pipeline. Versioning helps in tracking changes, ensuring compatibility across different environments, and providing clear markers for development milestones. By following a structured versioning approach, we can easily identify which versions of the application are in development, testing, or production.

#### Example Scenario:

Consider a scenario where a critical bug is identified in the production version of the My Demo App, which is tagged as `1.2.0`. The development team is currently working on new features for the next release, tagged as `1.3.0-dev`. With a clear versioning strategy in place, the team can quickly create a patch for the production version by branching from `1.2.0` and tagging the patched version as `1.2.1`. This allows the patch to be deployed to production while development on `1.3.0-dev` continues without disruption.

This approach ensures that bug fixes, new features, and updates are managed in a controlled and traceable manner, reducing the risk of conflicts and ensuring a smooth progression from development to production.

- **Semantic Versioning**: Use a versioning format like `MAJOR.MINOR.PATCH` (e.g., `1.0.0`, `0.2.0-dev`) to easily track changes and updates.
  - **MAJOR**: Incremented for incompatible API changes.
  - **MINOR**: Incremented for backwards-compatible functionality.
  - **PATCH**: Incremented for backwards-compatible bug fixes.
  - **Suffixes**: Use suffixes like `-dev`, `-alpha`, `-beta` for pre-release versions.
- **Build Metadata**: Consider adding build metadata (e.g., build timestamp or commit hash) to the image tags if needed, for example: `0.2.0-dev+20230829`.

This strategy helps in maintaining clear and meaningful version numbers that accurately represent the state and stability of the application at any given time.