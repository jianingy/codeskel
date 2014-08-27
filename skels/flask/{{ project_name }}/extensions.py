#!{{ python }}
# -*- coding: {{ encoding }} -*-
# {{ modeline }}
{{ license }}
# Author: {{ author }}

from oslo.config import cfg

database_opts = [
    cfg.StrOpt('connection',
               default='sqlite:///{{ project_name }}.db',
               help='The database connection string'),
]

CONF = cfg.CONF
CONF.register_cli_opts(database_opts, 'database')
CONF.register_opts(database_opts, 'database')

{% if plugin.flask_sqlalchemy -%}
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(session_options={'autocommit': True})

{% if plugin.flask_admin -%}
from flask.ext.admin import Admin
admin = Admin()
db_admin = SQLAlchemy(session_options={'autocommit': False})
{% endif -%}
{% endif -%}
