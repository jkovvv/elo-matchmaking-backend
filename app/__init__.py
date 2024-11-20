from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Inicijalizacija Flask-Migrate
    migrate = Migrate(app, db)

    # Registracija blueprint-a
    from .routes import bp
    app.register_blueprint(bp)

    return app
