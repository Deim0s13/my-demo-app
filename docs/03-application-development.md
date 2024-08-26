# Application Development

This document describes the steps taken to develop the My Demo App project.

## 1. Project Structure

The project is organized into the following structure:

```plaintext
my-demo-app/
├── docs/
├── src/
│   ├── backend/
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── extensions.py        # New file for managing extensions like SQLAlchemy
│   │   ├── models.py
│   │   ├── requirements.txt
│   │   └── migrations/
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
```

## 2. Environment Setup

### 2.1 Virtual Environment

The project uses a Python virtual environment to manage dependencies. The virtual environment should be set up in the `src/backend/` directory.

1. **Navigate to the Backend Directory**:
   - First, navigate to the `src/backend/` directory:
     ```bash
     cd src/backend
     ```

2. **Create and Activate the Virtual Environment**:
   - Create the virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```

3. **Install the Required Dependencies**:
   - Install the necessary Python packages:
     ```bash
     pip install -r requirements.txt
     ```

## 3. Database Setup

PostgreSQL is used as the database for this project. Below are the stops to setup and integrate the datbase with the Flask application.

### 3.1 Installing PostgreSQL

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

### 3.2 Setting up the Database

Create s new PostgreSQL database for the project
```bash
createdb <your-database-name>
```

** Optional: Create a new database user:
```bash
createuser -P -s -e <dbusername>
```

### 3.3 Configuring Flash to Use PosgreSQL

To configure the Flash application to connect to the PostgreSQL database using SQLAlchemy you need to create a 'config.py' file with the following connection string.

Note: We will look at removing the username and password from this later.
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://<your-database-user>:<your-password>@localhost/<your-database-name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 3.4 Setting up Flask-Migrate

Flask-Migrate was used to handle the database migration.

#### 3.4.1 Installing Dependencies

The following packages were installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate psycopg2-binary
```

#### 3.4.2 Initialise Flask-Migration

Flask-migration was initialised to create the 'migrations/' directory:
```bash
flask db init
```

#### 3.4.3 Create and Apply Initial Migration

The initial migration was created and applied to the set up database schema:

```bash
flask db migrate -m "Initial migration"
flask db upgrade
```

## 4. Backend Development

### 4.1 Restructuring for Cirtular Import Issue

To avoid circular import issues, we separated the database (db) initialization into a new file called extensions.py.

### 4.1.1 extensions.py

The extensions.py file is used to manage extensions like SQLAlchemy:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### 4.1.2 models.py

The models.py file defines the database models and imports db from extensions.py:
```python
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'
```

### 4.1.3 app.py

The app.py file imports db from extensions.py and initializes it within the application factory

## 5. Frontend Development

The frontend of the My Demo App project is located in the src/frontend/ directory. It includes HTML templates, CSS for styling, and JavaScript for interactivity.

### 5.1 Directory Structure

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

### 5.2 HTML Templates

The HTML templates handle pages for the homepage, user registration, login, and profile.

### 5.3 Static Files

CSS and JavaScript files are stored in the static/ directory.

### 5.4 Flask Integration

Flask was configured to serve the frontend from the src/frontend/ directory using the template_folder and static_folder parameters.

## 6. Running the Application

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

The application will be accessible at http://127.0.0.1:5000/.