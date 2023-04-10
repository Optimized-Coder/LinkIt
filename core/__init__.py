from flask import Flask
from .extensions import db
from flask_migrate import Migrate
import os
from dotenv import load_dotenv, find_dotenv


def create_app():
    load_dotenv(find_dotenv())

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_NAME')
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from .models import User

    # Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    app.app_context().push()

    return app

