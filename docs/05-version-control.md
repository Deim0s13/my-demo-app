# 5. Version Control
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

## 5.2 Preparing for Continuous Integration with Tekton

### 5.2.1 Introduction to Tekton

Tekton is a Kubernetes-native CI/CD solution that I’ll be using to automate the build and test processes for My Demo App. Even though I haven’t deployed to an OpenShift environment yet, setting up Tekton pipelines now will provide a strong foundation for future CI/CD implementations.

### 5.2.2 Initial Setup on a Local Environment

Since I’m currently working on a local environment (like a spare laptop running Single Node OpenShift (SNO)), I can start experimenting with Tekton by setting up a minimal pipeline:

   - **Install Tekton Pipelines**: I need to ensure that Tekton Pipelines are installed on my local OpenShift or Kubernetes cluster.
   - **Create Basic Tekton Tasks**: I’ll start with simple tasks, such as checking out the code from GitHub and running basic tests.

### 5.2.3 Expanding CI with Tekton on OpenShift

Once I transition to a more robust environment like ROSA, I plan to expand my Tekton pipelines to include more complex tasks, such as:

   - **Building Docker Images**: Automating the build process for my Docker images.
   - **Running Tests**: Integrating my testing framework into the pipeline to ensure code quality.

## 5.3 Future Considerations for Continuous Deployment

### 5.3.1 Planning for Deployment

When I’m ready to deploy my application to an OpenShift environment, I’ll expand my Tekton pipelines to include deployment tasks. This will likely involve:

   - **Deploying to OpenShift**: Using oc commands or Kubernetes manifests to deploy my application.
   - **Running Migrations**: Applying database migrations as part of the deployment proces

### 5.3.2 Incorporating GitOps with Argo CD

As I gain more experience with OpenShift, I’m considering integrating GitOps practices using Argo CD. This approach will allow me to manage deployments declaratively, with Git as the single source of truth.

## 5.4 Tagging and Prepartion for Deployment

In this section, I outline the steps taken to tag the current version of the My Demo App and ensure all changes are committed and ready for the next phase of the project.

### 5.4.1 Staging and Committing Changes

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

## 5.5 Versioning Strategy

To maintain a consistent versioning scheme throughout the development and deployment process, I’m using the following strategy:

- **Semantic Versioning**: Use a versioning format like `MAJOR.MINOR.PATCH` (e.g., `1.0.0`, `0.2.0-dev`) to easily track changes and updates.
  - **MAJOR**: Incremented for incompatible API changes.
  - **MINOR**: Incremented for backwards-compatible functionality.
  - **PATCH**: Incremented for backwards-compatible bug fixes.
  - **Suffixes**: Use suffixes like `-dev`, `-alpha`, `-beta` for pre-release versions.
- **Build Metadata**: Consider adding build metadata (e.g., build timestamp or commit hash) to the image tags if needed, for example: `0.2.0-dev+20230829`.

This strategy helps in maintaining clear and meaningful version numbers that accurately represent the state and stability of the application at any given time.