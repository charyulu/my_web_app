import sqlite3
from flask import g

# Path to your SQLite database file
DATABASE = "database.db"

def get_db():
    """
    Get a connection to the SQLite database.
    If no connection exists yet, create one and store it in the Flask `g` object.
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    """
    Close the database connection at the end of the request if it exists.
    """
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()