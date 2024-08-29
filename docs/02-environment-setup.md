# 2. Environment Setup

This document outlines the steps I took to set up the development environment for the My Demo App project.

## 2.1 Prerequisites

Before setting up the development environment, ensure that the following prerequisites are met:

- **Operating System**: The instructions provided are for macOS, but they can be adapted for other operating systems.
- **Python 3.11**: Python 3.11 should be installed on your machine.
- **PostgreSQL**: Ensure PostgreSQL is installed and running.
- **Git**: Git should be installed and configured on your system.
- **Environment Variables**: Sensitive data such as database credentials should be managed using environment variables.

## 2.2 Install Python 3.11

If Python 3.11 is not already installed, follow these steps:

### 2.2.1 macOS Installation

- **Using Homebrew**:
  - Update Homebrew:
    ```bash
    brew update
    ```
  - Install Python 3.11:
    ```bash
    brew install python@3.11
    ```

### 2.2.2 Verify Python Installation

- **Check Python Version**:
  - Ensure Python 3.11 is correctly installed:
    ```bash
    python3 --version
    ```

- **Set Up Python Path**:
  - If necessary, add Python 3.11 to your PATH environment variable.

## 2.3 Install Visual Studio Code (VS Code)

VS Code is the primary IDE used for this project.

- **Download and Install**:
  - Download VS Code from the [official website](https://code.visualstudio.com/Download) and install it on your machine.

- **Install Recommended Extensions**:
  - Launch VS Code and install the following extensions:
    - **Python**
    - **Docker**
    - **GitLens**
    - **Markdown All in One**

- **Configure VS Code**:
  - Adjust settings such as Python interpreter path and editor preferences as needed.

## 2.4 Install Podman

I’m using Podman to containerise the application.

- **Installation on macOS**:
  - Install Podman using Homebrew:
    ```bash
    brew install podman
    ```

  - Set up the Podman machine:
    ```bash
    podman machine init
    podman machine start
    ```

  - (Optional) Enable Docker CLI compatibility:
    ```bash
    alias docker=podman
    ```

- **Installation on Other OS**:
  - Follow the [official Podman installation guide](https://podman.io/getting-started/installation).

- **Verify Installation**:
  ```bash
  podman --version
  ```

## 2.5 Basic Introduction to Enviornment Variables

Environment variables are key-value pairs used by applications to configure settings and manage operational behavior without hard-coding these values directly into the code. They provide flexibility and security, especially when dealing with sensitive information like database credentials, API keys, and environment-specific settings (e.g., development, staging, production).

### 2.5.2 Why Use Environment Variables?

- **Separation of Configuration and Code**: Environment variables allow you to change configuration settings without modifying the code. This is especially useful when deploying the same codebase across different environments (development, staging, production).
- **Security**: Sensitive information like passwords and API keys can be managed outside the codebase, reducing the risk of exposing them in version control.
- **Portability**: Environment variables make your application more portable, as it can adapt to different environments by simply changing the variable values.

### 2.5.3 Setting Up Environment Variables

You can set up environment variables in several ways:

1.	**Directly in the Shell**:
You can set environment variables directly in your shell session. This is useful for temporary setups or quick tests.
```bash
export APP_ENV=development
export DATABASE_URL=postgresql://username:password@localhost/dbname
```

These variables will remain available for the current session.

2.	**Using a .env File**:
A `.env` file is a simple text file where you can store environment variables. This file should be located in the root directory of your project (or the relevant subdirectory). The `.env` file allows you to manage your environment variables in a central location.
Example .env file:
```plaintext
# .env file
APP_ENV=development
DATABASE_URL=postgresql://username:password@localhost/dbname
```

__Important__: The `.env` file should be added to your `.gitignore` file to prevent sensitive information from being exposed in your version control system.

```plaintext
# .gitignore
.env
```

3.	**Accessing Environment Variables in Code**:
Environment variables can be accessed in your Python code using the os module.
Example in `app.py`:
```python
import os

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
```

This allows your application to dynamically adapt based on the environment it’s running in, simply by changing the environment variable values.

### 2.5.4 Example Environment Variables

Here are some common environment variables you might use in your project:

- **APP_ENV**: Defines the environment the application is running in (e.g., development, staging, production).
- **DATABASE_URL**: Connection string for your PostgreSQL database.
- **SECRET_KEY**: A secret key used by Flask for session management and other cryptographic operations.

Example .env file:
```plaintext
APP_ENV=development
DATABASE_URL=postgresql://mydemoappuser:password@localhost/mydemoapp_db
SECRET_KEY=your_secret_key_here
```

### 2.5.5 Security Considerations

While environment variables offer a more secure way to manage sensitive information, they are not foolproof:

- **Protect the `.env` File**: Always add the `.env` file to your `.gitignore` to ensure it doesn’t get committed to your version control.
- **Use Encryption**: Consider encrypting sensitive values in your environment variables or using secret management tools for production environments.

## 2.6 Configure Cypress

I am using Cypress to perform end-to-end testing of the application. The [06 Testing](06-testing.md) section provides more details on how this has been used.

However, I've provided some details on the installation and configuration of Cypress here:

### 2.6.1 Installation

  - Navigate to the `src/frontend/` directory:
    ```bash
    cd src/frontend/
    ```

  - Install Cypress as a development dependency:
    ```bash
    npm install cypress --save-dev
    ```

### 2.6.2 Configuration

  - Create a Cypress configuration file named `cypress.config.js` in the `src/frontend/` directory. Below is an example configuration:
    ```javascript
    const { defineConfig } = require("cypress");

    module.exports = defineConfig({
      e2e: {
        baseUrl: 'http://localhost:5001',
        setupNodeEvents(on, config) {
          // implement node event listeners here
        },
        video: false,
        screenshotsFolder: 'cypress/screenshots',
        videosFolder: 'cypress/videos',
      },
    });
    ```

### 2.6.3 Running Cypress

  - To run Cypress tests, use the following command in the `src/frontend/` directory:
    ```bash
    npx cypress open
    ```
  - This will open the Cypress Test Runner where you can execute your tests.

## 2.7 .gitignore Contents

```plaintext
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Virtual environments
venv/
.venv/

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# pipenv
# According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
# However, in case you generate the Pipfile.lock file in some other way, you should ignore it.
# Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# VS Code files
.vscode/

# MacOS files
.DS_Store

# Node.js related files
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json

# Jest related files
jest/
coverage/
*.snap

# Cypress related files
cypress/videos/
cypress/screenshots/

# Logs
logs/
*.log
*.log.*

# Temporary files
tmp/
temp/
*.tmp
```

__Explanation of .gitignore Entries__

- **Byte-compiled / optimised / DLL files**: Excludes Python bytecode files and any compiled Python extensions.
- **Virtual environments**: Excludes directories for virtual environments to avoid committing local environment-specific files.
- **Distribution / packaging**: Excludes files related to Python packaging, which are generated during the build process.
- **Installer logs**: Excludes logs generated by `pip` during installation.
- **Unit test / coverage reports**: Excludes directories and files related to unit testing and code coverage.
- **Jupyter Notebook**: Excludes automatically generated backup files from Jupyter Notebooks.
- **pyenv**: Excludes `.python-version`, a file used by `pyenv` to specify Python versions.
- **VS Code files**: Excludes configuration files specific to Visual Studio Code, which I don’t need in the repository.
- **MacOS files**: Excludes `.DS_Store`, a system file generated by macOS.
- **Node.js related files**: Excludes `node_modules/` and log files that are generated during `npm` or `yarn` operations.
- **Jest related files**: Excludes coverage reports and snapshots generated by Jest.
- **Cypress related files**: Excludes videos and screenshots generated during Cypress test runs.
- **Logs and Temporary Files**: Excludes general log files and temporary directories.