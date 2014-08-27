# -*- coding: {{ encoding }} -*-
# {{ modeline }}
{{ license }}
# Author: {{ author }}

from datetime import datetime

def utcnow():
    return datetime.utcnow()
