from flask import Flask
from flask_cors import CORS
from .models import db
from .routes import bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # Enable CORS
    db.init_app(app)

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
