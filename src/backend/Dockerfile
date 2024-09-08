# Dockerfile for Backend

# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Build argument for version and environment
ARG VERSION
ARG ENVIRONMENT

# Set the working directory in the container
WORKDIR /app

# Copy the backend files into the container
COPY . /app/backend/

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

# Load the .env file and define the command to run the application with migrations
CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]