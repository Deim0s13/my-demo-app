# Use an official Node.js image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the frontend files into the container
COPY . /app

# Install dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "start"]