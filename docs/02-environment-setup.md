# Environment Setup

This document outlines the steps to set up the development environment for the My Demo App project.

## 1. Install Visual Studio Code (VS Code)

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

## 2. Install Podman

Podman is used for containerizing the application.

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

  ### Step 3: **Commit and Push the Documentation**

1. **Add and Commit the Documentation**:
   - Add the updated documentation file to Git:
     ```bash
     git add docs/02-environment-setup.md
     ```
   - Commit the changes:
     ```bash
     git commit -m "Documented VS Code, Podman, and Git setup"
     ```

2. **Push to GitHub**:
   - Push the changes to your GitHub repository:
     ```bash
     git push origin main
     ```
