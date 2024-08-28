# 4 Containerisation
This section outlines the steps I took to containerise the My Demo App using Podman. Containerising the application ensures it is portable and can be easily deployed across different environments..

## 4.1 Creating the Dockerfile

The `Dockerfile` is located in the `src/` directory and is used to build a container image for the My Demo App. This file specifies the base image, copies the application code, installs dependencies, and defines the command to run the application.

__Key Points__:

- **Base Image**: The Dockerfile uses python:3.11-slim as the base image for a lightweight and efficient container.
- **Dependencies**: All necessary Python dependencies are installed within the container using the requirements.txt file.
- **Working Directory**: The application files are organised within the /app directory in the container.
- **Port Configuration**: The application listens on port 5000 within the container, though this can be mapped to different host ports as needed.

For detailed instructions on building and running the container, see the following sections.

## 4.2 Building the Container Image

After the Dockerfile is ready, I used Podman to build the container image.

__Steps__:

1.	**Build the Image**:
  - Run the following command to build the container image:
```bash
podman build -t my-demo-app .
```

This command creates an image named `my-demo-app` using the current directory as the build context.

2. **Verify the Image**:
   - Verify that the image was successfully created by listing your Podman images:
```bash
podman images
```

You should see `my-demo-app` listed among the images

## 4.3 Running the Container
Once the image is built, you can run the container.

__Steps__:

1. **Create a Podman Network** (If needed):

If the container needs to communicate with a PostgreSQL container or other services, create a network:
```bash
podman network create mydemoapp_net
```

2. **Run the Database Container**:
I started the PostgreSQL database container (assuming it’s named mydemoapp_db):
```bash
podman run -d --name mydemoapp_db --network mydemoapp_net -e POSTGRES_USER=mydemoappuser -e POSTGRES_PASSWORD=passwordpassword -e POSTGRES_DB=mydemoapp_db postgres:14
```

3. **Run the Container**:
Use the following command to run the container:
```bash
podman run --name mydemoapp --network mydemoapp_net -e DATABASE_URL=postgresql://mydemoappuser:passwordpassword@mydb:5432/mydemoapp_db -p 5001:5000 my-demo-app
```

This runs the container in detached mode (-d), with port `5001` on the host mapped to port `5000` in the container:
- **Note**: Port 5000 was already in use, so port 5001 was used instead.

4. **Verify the Container is Running**:
Check that the container is running:
```bash
podman ps
```

You should see `my-demo-app` listed as running.

5. **Access the Application**:
Open your web browser and navigate to `http://localhost:5001/` to see the application running in the container.

## 4.4 Applying Database Migrations inside the Container

After running the container, I needed to apply database migrations to ensure the database schema was up to date.

__Steps__:

1. **Access the Running Container**:
Access the running container to run the migrations:
```bash
podman exec -it mydemoapp bash
```

2. **Run the Migrations**:
Once inside the container, run the `Flask-Migration` commands:
```bash
flask db upgrade
```
3. **Exit the Container**:
After running the migration, exit the container:
```bash
exit
```

## 4.5 Stopping and Removing the Container (Optional)

If you need to stop or remove the container, follow these steps:

1.	**Stop the Container**:
To stop the running container, use the following command:
```bash
podman stop <container_id>
```

Replace <container_id> with the actual container ID.

2. **Remove the Container**:
To remove the stopped container.
```bash
podman rm <container_id>
```