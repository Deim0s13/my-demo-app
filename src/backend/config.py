import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'

    # Load the database settings from environment variables
    DB_USER = os.getenv('DB_USER', 'mydemoappuser')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'mydemoapp_db')

    # Construct the database URL
    if os.environ.get('FLASK_ENV') == 'production':
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False