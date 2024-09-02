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