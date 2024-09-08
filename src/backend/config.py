import os

class Config:
    # Load the secret key from an environment variable or use a default value
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_secret_key')

    # Retrieve database credentials from environment variables
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME')

    # Construct the database URI using environment variables
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Optionally track modifications (set to False for production)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Handle environment-based configuration
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    if FLASK_ENV == 'production':
        print("Running in production mode.")
    else:
        print("Running in development mode.")