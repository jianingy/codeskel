from .extensions import db as flask_db

def get_metadata():
    return flask_db.metadata

def get_session():
    return flask_db.session
