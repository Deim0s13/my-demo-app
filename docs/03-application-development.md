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
│   │   ├── requirements.txt
│   │   └── templates/
│   │       └── index.html
│   ├── frontend/
│   ├── database/
├── .github/
│   └── workflows/
```

## 2. Creating the Flash Applicatin

### 2.1 Backend Setup
The backend is built using Flask, a lightweight Python web framework.

- app.py: Contains the main application logic, with two routes:
  - /: Serves the index.html file.
  - /data: Returns a JSON response with a message.
- requirements.txt: Lists the project dependencies, starting with Flask.

### 2.2 Frontend Setup

The frontend consists of a simple HTML file (index.html) that displays a welcome message.

## 3. Running the Application

To run the application locally:

1. Navigate to src/backend directory
2. Activate the virtual environment
```bash
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the Flash application
```bash
python app.py
```

Open a browser and visit http://127.0.0.1:5000/ to see the application in action.

## 4. Database Setup

PostgreSQL is used as the database for this project. Below are the stops to setup and integrate the datbase with the Flask application.

### 4.1 Installing PostgreSQL

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

### 4.2 Setting up the Database

Create s new PostgreSQL database for the project
```bash
createdb <your-database-name>
```

** Optional: Create a new database user:
```bash
createuser -P -s -e <dbusername>
```

### 4.3 Configuring Flash to Use PosgreSQL

To configure the Flash application to connect to the PostgreSQL database using SQLAlchemy you need to create a 'config.py' file with the following connection string.

Note: We will look at removing the username and password from this later.
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://<your-database-user>:<your-password>@localhost/<your-database-name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 4.4 Setting up Flask-Migrate

Flask-Migrate was used to handle the database migration.

#### 4.4.1 Installing Dependencies

The following packages were installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate psycopg2-binary
```

#### 4.4.2 Initialise Flask-Migration

Flask-migration was initialised to create the 'migrations/' directory:
```bash
flask db init
```

#### 4.4.3 Create and Apply Initial Migration

The initial migration was created and applied to the set up database schema:

```bash
flask db migrate -m "Initial migration"
flask db upgrade
```

### Running the Application

With the database set up and integrated, the Flask application was run to verify the connection:
```bash
flask run
```
