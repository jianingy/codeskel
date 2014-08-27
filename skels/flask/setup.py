#!{{ python }}
# -*- coding: {{ encoding }} -*-
# {{ modeline }}
{{ license }}
# Author: {{ author }}

from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,
)
