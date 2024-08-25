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
