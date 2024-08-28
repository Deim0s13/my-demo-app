# 2. Environment Setup

This document outlines the steps I took to set up the development environment for the My Demo App project.

## 2.1 Prerequisites

Before setting up the development environment, ensure that the following prerequisites are met:

- **Operating System**: The instructions provided are for macOS, but they can be adapted for other operating systems.
- **Python 3.11**: Python 3.11 should be installed on your machine.
- **PostgreSQL**: Ensure PostgreSQL is installed and running.
- **Git**: Git should be installed and configured on your system.

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

## 2.5 Configure Cypress

I am using Cypress to perform end-to-end testing of the application. The [06 Testing](06-testing.md) section provides more details on how this has been used.

However, I've provided some details on the installation and configuration of Cypress here:

### 2.5.1 Installation

  - Navigate to the `src/frontend/` directory:
    ```bash
    cd src/frontend/
    ```

  - Install Cypress as a development dependency:
    ```bash
    npm install cypress --save-dev
    ```

### 2.5.2 Configuration

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

### 2.5.3 Running Cypress

  - To run Cypress tests, use the following command in the `src/frontend/` directory:
    ```bash
    npx cypress open
    ```
  - This will open the Cypress Test Runner where you can execute your tests.

## 2.6 .gitignore Contents

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