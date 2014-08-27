# -*- coding: {{ encoding }} -*-
# {{ modeline }}
{{ license }}
# Author: {{ author }}

def boxquote(title, body):
    length = 78
    padding = '=' * ((length - len(title)) / 2)
    top = '%s %s %s' % (padding, title, padding)
    bottom = '^' * length
    return '%s\n%s\n%s' % (top[:length], body, bottom)
