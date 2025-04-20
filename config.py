class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"  # Replace with your open-source DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False