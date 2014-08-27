# -*- coding: utf-8 -*-
#
# Copyright 2014, Jianing Yang
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from jinja2 import Template
import os
from oslo.config import cfg
import pkg_resources
import sys

__version__ = pkg_resources.require('codeskel')[0].version
cli_opts = [
    cfg.StrOpt('python',
               default='python2.7',
               help='default python interpretor'),
    cfg.StrOpt('encoding',
               default='UTF-8',
               help='default encoding of python scripts'),
    cfg.StrOpt('modeline',
               default='vim: ts=4 sw=4 ai et',
               help='modeline for editor'),
    cfg.StrOpt('license', default='LICENSE', help='license file'),
    cfg.StrOpt('author', default='', help='project author'),
    cfg.StrOpt('source', required=True, help='skeleton source directory'),
    cfg.StrOpt('project_name', positional=True)
]

plugin_opts = [
    cfg.BoolOpt('flask-sqlalchemy', default=True, help='enable flask db'),
    cfg.BoolOpt('flask-admin', default=True, help='enable flask admin'),
]

CONF = cfg.CONF
CONF.register_cli_opts(cli_opts)
CONF.register_cli_opts(plugin_opts, 'plugin')


def main():
    CONF(sys.argv[1:], project='codeskel', version=__version__)

    if os.path.exists(CONF.license):
        license = file(CONF.license).read()
        license = "\n".join(map(lambda x: '# ' + x, license.splitlines()))
        CONF.set_override('license', license)
    else:
        CONF.set_override('license', '')

    for root, dirs, files in os.walk(CONF.source):
        for filename in files:
            base = root[len(CONF.source) + 1:]  # +1 for trailing slash
            source = os.path.join(root, filename)
            target = Template(os.path.join(CONF.project_name, base,
                                           filename)).render(CONF)
            print source, "-->", target
            dirname = os.path.dirname(target)
            if not os.path.isdir(dirname):
                os.makedirs(dirname, mode=0755)
            if not os.path.exists(target):
                try:
                    source_code = Template(file(source).read()).render(CONF)
                    file(target, "w+").write(source_code)
                except Exception as e:
                    print "Error processing: ", source, str(e)
