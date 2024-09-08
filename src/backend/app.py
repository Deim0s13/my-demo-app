from flask import Flask, render_template, request, redirect, url_for # type: ignore
from extensions import db
from models import User
from config import Config
from flask_migrate import Migrate # type: ignore
import os
import sys
import base64
from dotenv import load_dotenv # type: ignore
from pathlib import Path

def create_app():
    # Define the root directory (parent directory of backend)
    root_dir = Path(__file__).resolve().parent.parent

    # Load environment variables from the .env file in the root directory
    load_dotenv(dotenv_path=root_dir / '.env')

    app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
    app.config.from_object(Config)

    # Decode the DB password from the environment variable (if encoded)
    db_password = os.getenv('DB_PASSWORD')
    if db_password:
        db_password = base64.b64decode(os.getenv('DB_PASSWORD')).decode('utf-8')

    # Update SQLAlchemy database URI with decoded password and environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USER')}:{db_password}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    db.init_app(app)
    migrate = Migrate(app, db)

    # Environment and version check
    if os.getenv('APP_ENV') == 'development':
        print(f"Warning: You are running a development version of the application (Version: {os.getenv('APP_VERSION')}).")
        if os.getenv('ALLOW_DEPLOY_TO_NON_PROD') != 'true':
            sys.exit("Error: Deployment of development version to non-prod/prod is not allowed.")
    elif os.getenv('APP_ENV') == 'production':
        print(f"Running in production mode (Version: {os.getenv('APP_VERSION')}).")

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('profile', user_id=new_user.id))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            user = User.query.filter_by(username=username).first()
            if user:
                return redirect(url_for('profile', user_id=user.id))
        return render_template('login.html')

    @app.route('/profile/<int:user_id>')
    def profile(user_id):
        user = User.query.get_or_404(user_id)
        return render_template('profile.html', user=user)

    @app.route('/edit_profile', methods=['GET', 'POST'])
    def edit_profile():
        # Placeholder for profile editing functionality
        return "Edit profile page coming soon..."

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)