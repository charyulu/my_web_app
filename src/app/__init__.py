from flask import Flask
import os
app = Flask(__name__)
#export FLASK_SECRET_KEY="your_secure_key_here"
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Import and register blueprints
from .routes import auth
app.register_blueprint(auth.bp)

# Export the app object
__all__ = ['app']