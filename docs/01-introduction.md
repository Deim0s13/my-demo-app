# 1. Introduction
## 1.2 Overview

My Demo App is a web application designed to demonstrate the full lifecycle of developing, deploying, and managing a Python-based web application using the Flask framework and PostgreSQL database. My Demo App showcases best practices in software development, including environment setup, database management, frontend-backend integration, containerisation using Podman, and deployment readiness.

## 1.3 Features

- **User Management**: The application includes basic user management features, such as user registration, login, and profile management. Users can sign up with a username and email, log in, and view or update their profile information.
- **PostgreSQL Integration**: The backend is powered by a PostgreSQL database, providing robust data storage and retrieval capabilities. I demonstrate how to set up and interact with a relational database using SQLAlchemy and Flask-Migrate for database migrations, both in native and containerised environments
- **Frontend-Backend Integration**: The application includes a simple, yet functional, frontend built with HTML, CSS, and JavaScript. The frontend interacts with the backend through RESTful API endpoints, demonstrating the flow of data between the user interface and the server.
- **Modular Architecture**: The project is structured to separate concerns effectively. The backend, frontend, and database layers are clearly defined, making the application easy to manage, extend, and deploy.
- **Deployment Readiness**: I’ve designed the project with deployment in mind, including containerisation using Podman. There are clear instructions on setting up the environment, managing dependencies, and running the application locally, in a containerised environment, and in production

## 1.4 Purpose

This application serves as a practical example for developers like myself who want to understand the complete process of building a web application, from initial setup to deployment, including containerisation techniques.