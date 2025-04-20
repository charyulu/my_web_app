from flask import Flask
from src.app.db import close_connection


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
# Register the function to close the database connection
    # Import and register blueprints
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    @app.teardown_appcontext
    def teardown_db(exception):
        close_connection(exception)

    return app
