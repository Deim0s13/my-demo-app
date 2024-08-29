# 4 Containerisation
This section outlines the steps I took to containerise the My Demo App using Podman and `podman-compose`. Containerising the application ensures it is portable and can be easily deployed across different environments.

## 4.1 Creating the Dockerfile

The project contains two separate `Dockerfiles—one` for the backend and one for the frontend. These files are located in their respective directories under `src/` and are used to build container images for each service.

### 4.1.1 Backend Dockerfile

The backend Dockerfile is located in the `src/backend/` directory. This file specifies the base image, copies the backend application code, installs dependencies, and defines the command to run the application.

__Key Points__:

- **Base Image**: The Dockerfile uses `python:3.11-slim` as the base image for a lightweight and efficient container.
- **Dependencies**: All necessary Python dependencies are installed within the container using the `requirements.txt` file.
- **Working Directory**: The application files are organised within the `/app/backend` directory in the container.
- **Port Configuration**: The backend application listens on port `5000` within the container.
- **Database Migrations**: The Dockerfile includes a command to automatically run database migrations when the container starts.

__Backend Dockerfile Contents__:
```dockerfile
# Dockerfile for Backend

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Build argument for version and environment
ARG VERSION
ARG ENVIRONMENT

# Set the working directory in the container
WORKDIR /app

# Copy the backend files into the container
COPY backend/ /app/backend/

# Set the working directory for the backend
WORKDIR /app/backend

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=$ENVIRONMENT
ENV APP_VERSION=$VERSION

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application with migrations
CMD flask db upgrade && flask run --host=0.0.0.0
```

### 4.1.2 Frontend Dockerfile

The frontend Dockerfile is located in the `src/frontend/` directory. This file specifies the base image, copies the frontend application code, installs dependencies, and defines the command to start the frontend application.

#### Key Points:

- **Base Image**: The Dockerfile uses `node:18-alpine` as the base image for a lightweight and efficient container.
- **Dependencies**: All necessary Node.js dependencies are installed within the container using `npm install`.
- **Working Directory**: The application files are organised within the `/app/frontend` directory in the container.
- **Port Configuration**: The frontend application listens on port `3000` within the container.

__Frontend Dockerfile Contents__:
```dockerfile
# Dockerfile for Frontend

# Use an official Node.js image
FROM node:18

# Build argument for version
ARG VERSION

# Set the working directory in the container
WORKDIR /app

# Copy the frontend files into the container
COPY . /app

# Set environment variables
ENV APP_VERSION=$VERSION

# Install dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "start"]
```

## 4.2 Setting Up podman-compose

To streamline the process of running multiple containers (such as the backend and database), I used `podman-compose`, which allows defining and running multi-container applications.

__Steps:__

1. **Install podman-compose**:
If you haven’t installed `podman-compose`, you can do so using pip:
```bash
pip install podman-compose
```

2.	**Create a docker-compose.yml File**:
The `docker-compose.yml` file defines the services (backend, database, frontend) and their configurations. This file is located in the `src/` directory.

__Key Points__:

- The file specifies the build contexts for the backend and frontend services.
- The `depends_on` directive ensures that the backend service waits for the database to be ready.
- The database service uses environment variables to set up the PostgreSQL user, password, and database.
- 
3.	**Using podman-compose to Build and Run the Containers**:
With the docker-compose.yml file in place, the following command is used to build and start all services:
```
podman-compose up --build
```

4. **Verify the Setup**:
After running the `podman-compose` command, you can check that the containers are running with:
```bash
podman ps
```
You should see the services (mydemoapp_backend, mydemoapp_db, and mydemoapp_frontend) listed and running.

## 4.3 Applying Database Migration Automatically

To automate the application of database migrations:

1. **Automated Migrations**:
The Dockerfile for the backend service includes a command that runs database migrations automatically when the container starts:
```bash
CMD flask db upgrade && flask run --host=0.0.0.0
```

This ensures that the database schema is always up to date when the application starts.

2.	**Manual Migrations (if needed)**:
If you ever need to run migrations manually, you can access the backend container:
```bash
podman exec -it mydemoapp_backend bash
```

Then, run the migration command:
```bash
flask db upgrade
```

## 4.5 Stopping and Removing the Container (Optional)

If you need to stop or remove the container, follow these steps:

1. **Stop the Container**:
   To stop the running container, use the following command:
   ```bash
   podman stop <container_id>
   ```

Replace <container_id> with the actual container ID.

2.	**Remove the Container**:
To remove the stopped container, use the following command:
   To stop the running container, use the following command:
   ```bash
   podman rm <container_id>
   ```

Replace <container_id> with the actual container ID.