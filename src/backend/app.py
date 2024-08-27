from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import User
from config import Config
from flask_migrate import Migrate  # Add this import

def create_app():
    app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)  # Initialize Flask-Migrate with your app and db

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