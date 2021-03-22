#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit-libs-{{cookiecutter.lib_name}}
"""

import pytest

from tpRigToolkit.libs.{{cookiecutter.lib_name}} import __version__


def test_version():
    assert __version__.get_version()
