#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpRigToolkit-libs-{{cookiecutter.lib_name}}
"""

from __future__ import print_function, division, absolute_import

import os
import logging.config

from tpDcc.core import library

from tpRigToolkit.libs.{{cookiecutter.lib_name}}.core import consts


class {{cookiecutter.lib_class}}Lib(library.DccLibrary, object):

    ID = consts.LIB_ID

    def __init__(self, *args, **kwargs):
        super({{cookiecutter.lib_class}}Lib, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls):
        base_tool_config = library.DccLibrary.config_dict()
        tool_config = {
            'name': '{{cookiecutter.lib_nice_name}}',
            'id': cls.ID,
            'supported_dccs': {{cookiecutter.supported_dccs}},
            'tooltip': '{{cookiecutter.lib_description}}'
        }
        base_tool_config.update(tool_config)

        return base_tool_config