import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'

    # Adjust database URL depending on the environment
    if os.environ.get('FLASK_ENV') == 'production':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://mydemoappuser:password@db/mydemoapp_db'
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://mydemoappuser:password@localhost/mydemoapp_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False