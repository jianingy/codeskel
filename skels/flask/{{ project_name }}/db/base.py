from .extensions import db as flask_db
import sqlalchemy as sa

class BASE(flask_db.Model, db.TableNameMixin):
    __abstract__ = True
