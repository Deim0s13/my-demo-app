# 6. Testing

This section outlines the testing strategy for the My Demo App project, covering both backend and frontend tests. Testing ensures that the application functions as expected and helps identify any issues before deployment.

## 6.1 Pre-requisites

Before running the tests, ensure you have the following installed and set up:

- Python (ensure your virtual environment is activated)
- Flask and related dependencies (from `requirements.txt`)
- PostgreSQL running and configured
- Cypress installed for frontend testing (`npm install cypress --save-dev`)
- Environment Variables: Ensure that environment variables such as `APP_ENV` and `APP_VERSION` are set correctly before running tests.

## 6.2 Backend Testing with Pytest

Pytest is used for testing the backend functionality of the My Demo App. These tests ensure that the application logic, database interactions, and API endpoints work correctly.

### 6.2.1 Running Tests on the Native App

To run the backend tests against the native (non-containerized) version of the application:

1. **Ensure PostgreSQL is Running**:
   - Start the PostgreSQL service:
   ```bash
   brew services start postgresql@14
   ```

2. **Validate the Virtual Environment**:
    Navigate to the `src/backend/` directory:
    ```bash
    cd src/backend
    ```

3. **Set Environment Variables**:
Ensure that `APP_ENV` and `APP_VERSION` are set before running the tests:
```bash
export APP_ENV=<Correct Environment, e.g. development>
export APP_VERSION=<Correct Version, e.g. 0.2.0-dev>
```

3. **Run Pytest**:
   Execute the backend tests:
   ```bash
   pytest
   ```

Pytest will automatically discover and run the tests located in the `src/backend/__tests__/ directory`. Ensure that your test files are named appropriately (e.g., test_routes.py) and contain test functions prefixed with test_.

### 6.2.2 Running Tests on the Containerised App

To run the backend tests against the containerised version of the application:

1. **Ensure the Containerised App is Running**
    To run the backend tests against the containerised version of the application:
    ```bash
    podman-compose up --build
    ```

2. **Run Pytest**:
    Use the following command to run the tests against the containerised app:
    ```bash
    pytest
    ```

Ensure that the tests connect to the containerized database and application. Pytest will execute the tests located in the `src/backend/__tests__/ directory`.

## 6.3 Frontend Testing with Cypress

Cypress is used for end-to-end testing of the frontend. These tests ensure that the user interface behaves as expected.

### 6.3.1 Running Cypress Tests on the Native App

To run the Cypress tests against the native (non-containerized) version of the application:

1. **Ensure the Native App is Running**:
    Start the application using Flask:
    ```bash
    podman-compose up --build
    ```

2. **Run Cypress Test**:
    Execute the Cypress tests using the following command:
    ```bash
    npx cypress run --env APP_ENV=development,APP_VERSION=0.2.0-dev
    ```

Ensure that the containerized app is accessible at `http://localhost:5001`. Cypress will run the tests located in the `src/frontend/cypress/e2e/` directory against this instance of the application. The key test files are:
   - `login_spec.cy.js`
   - `register_spec.cy.js`

## 6.4 Managing Test Results

### 6.4.1 Viewing Test Results

After running the tests, you can view the results directly in the terminal. Cypress and Pytest will display the number of tests passed, failed, and skipped, along with detailed error messages for any failures.

### 6.4.2 Troubleshooting

- **Common Issues**:
  - **Database connection errors**: Ensure that the database is correctly configured and accessible from the application.
  - **Port conflicts**: Verify that the application is running on the correct port and that no other services are using the same port.
  - **Environment variable issues**: Double-check that all necessary environment variables are set, especially `DATABASE_URL`.
  - **Environment variable issues**: Double-check that all necessary environment variables are set, especially `DATABASE_URL`, `APP_ENV`, and `APP_VERSION`.

- **Accessing Logs**:
  - For Pytest errors, review the traceback provided in the terminal.
  - For Cypress errors, review the screenshots and videos generated in the `cypress/screenshots/` and `cypress/videos/` directories.