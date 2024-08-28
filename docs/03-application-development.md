# 3. Application Development

This document describes the steps I took to develop the My Demo App project.

## 3.1 Project Structure

The project is organized into the following structure:

```plaintext
my-demo-app/
├── docs/
├── src/
│   ├── backend/
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── extensions.pyWas
│   │   ├── models.py
│   │   ├── requirements.txt
│   │   ├── migrations/
│   │   ├── __tests__/
│   │   │   ├── test_routes.py
│   │   │   ├── test_models.py
│   ├── frontend/
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   ├── register.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── styles.css
│   │   │   ├── js/
│   │   │   │   └── scripts.js
│   │   ├── cypress/
│   │   │   ├── e2e/
│   │   │   │   ├── login_spec.cy.js
│   │   │   │   ├── register_spec.cy.js
│   │   │   ├── fixtures/
│   │   │   ├── support/
```

## 3.2 Environment Setup

### 3.2.1 Virtual Environment

I used a Python virtual environment to manage dependencies. The virtual environment is set up in the `src/backend/` directory

1. **Navigate to the Backend Directory**:
   First, navigate to the `src/backend/` directory:
   ```bash
   cd src/backend
   ```

2. **Create and Activate the Virtual Environment**:
   Create the virtual environment:
   ```bash
    python3 -m venv venv
    ```
    
    Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

1. **Install the Required Dependencies**:
    Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## 3.3 Database Setup

I used PostgreSQL as the database for this project. Below are the steps I took to set up and integrate the database with the Flask application.

### 3.3.1 Installing PostgreSQL

PostgreSQL was installed using Homebrew on macOS.
```bash
brew update
brew install postgresql@14
```

Start the PostgreSQL service:
```bash
brew services start postgresql@14
```

If this is the first time PostgreSQL is being set up, initialise the database.
```bash
initdb /usr/local/var/postgres
```

### 3.3.2 Setting up the Database

I Create a new PostgreSQL database for the project
```bash
createdb <your-database-name>
```

** Optional: Create a new database user:
```bash
createuser -P -s -e <dbusername>
```

### 3.3.3 Configuring Flash to Use PosgreSQL

To configure the Flask application to connect to the PostgreSQL database using SQLAlchemy, I defined the connection string in the config.py file.

For detailed code, please refer to the config.py file in the Git repository.

__Note__: We will look at removing the username and password from this later.

### 3.3.4 Setting up Flask-Migrate

I used Flask-Migrate to handle the database migration.

#### 3.3.4.1 Installing Dependencies

The following packages were installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate psycopg2-binary
```

#### 3.3.4.2 Initialise Flask-Migration

Flask-migration was initialised to create the 'migrations/' directory:
```bash
flask db init
```

#### 3.3.4.3 Create and Apply Initial Migration

The initial migration was created and applied to the set up database schema:

```bash
flask db migrate -m "Initial migration"
flask db upgrade
```

## 3.4 Backend Development

### 3.4.1 Restructuring for Cirtular Import Issue

To avoid circular import issues, I separated the database (db) initialisation into a new file called `extensions.py`.

### 3.4.1.1 extensions.py

The `extensions.py` file is used to manage extensions like SQLAlchemy:
```python
from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()
```

### 3.4.1.2 models.py

The `models.py` file defines the database models and imports db from `extensions.py`:
```python
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'
```

### 3.4.1.3 app.py

The `app.py` file imports db from `extensions.py` and initializes it within the application factory

## 3.5 Frontend Development

The frontend of the My Demo App project is located in the `src/frontend/` directory. It includes HTML templates, CSS for styling, and JavaScript for interactivity.

### 3.5.1 Directory Structure

The frontend is organized as follows:

```plaintext
src/
├── frontend/
│   ├── templates/
│   │   ├── index.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── profile.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
```

### 3.5.2 HTML Templates

The HTML templates handle the structure and layout of the pages users interact with. Below is a brief description of each file and its purpose:

- **index.html**: The homepage of the application, welcoming users and providing links to register or log in. It serves as the starting point for navigating the application.
- **register.html**: The registration page, where new users can sign up by providing a username and email. This form sends data to the backend to create a new user account.
- **login.html**: The login page, where users can enter their username to log in. Upon successful login, users are redirected to their profile page.
- **profile.html**: The profile page displays the user’s information, such as their username and email. It allows users to view their details and provides a link to edit their profile in the future.

### 3.5.3 Static Files

- **styles.css**: This CSS file contains the styles used throughout the application, ensuring a consistent look and feel across all pages.
- **scripts.js**: This JavaScript file is currently a placeholder for future client-side functionality that might be added to enhance user interactions.

### 3.5.4 Flask Integration

Flask was configured to serve the frontend from the src/frontend/ directory using the template_folder and static_folder parameters. This allows the Flask backend to render these HTML templates and serve the static files appropriately.

## 3.6 Running the Application

To run the application, follow these steps:

1.	**Ensure PostgreSQL is running**:
```bash
  brew services start postgresql@14
```

2. **Activate the virtual environment**:
```bash
source venv/bin/activate
```

3. **Run the Flask application**:
```bash
flash run
```

The application will be accessible at http://127.0.0.1:5001/.