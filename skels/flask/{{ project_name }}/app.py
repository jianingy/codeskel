{% if plugin.flask_sqlalchemy -%}
from .extensions import db
{% if plugin.flask_admin -%}
from .extensions import db_admin
{% endif -%}
{% endif -%}
from . import filters

from flask import Flask
from oslo.config import cfg

application_opts = [
    cfg.BoolOpt('debug', default=False, help='Enable debug mode'),
]

CONF = cfg.CONF
CONF.register_cli_opts(application_opts)
CONF.register_opts(application_opts)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.database.connection

    filters.init_app(app)
    {% if plugin.flask_sqlalchemy -%}
    db.init_app(app)
    {% if plugin.flask_admin -%}
    db_admin.init_app(app)
    admin.init_app(app)
    {% endif -%}
    {% endif -%}

    # app.register_blueprint(blueprint)
    # admin.add_view(adminview)

    return app
