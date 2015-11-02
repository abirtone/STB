# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

import six

from sys import version_info
from termcolor import colored

from .data import *

__version__ = "1.0.0"
__all__ = ["run_console", "run", "GlobalParameters"]


# --------------------------------------------------------------------------
#
# Command line options
#
# --------------------------------------------------------------------------
def run_console(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    six.print_(colored("[*]", "blue"), "Starting {{ cookiecutter.tool_name }} execution")
    run(config)
    six.print_(colored("[*]", "blue"), "Done!")


# ----------------------------------------------------------------------
#
# API call
#
# ----------------------------------------------------------------------
def run(config):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    {%- if cookiecutter.python_version_3 != cookiecutter.python_version_2 %}
    # --------------------------------------------------------------------------
    # Checks Python version
    # --------------------------------------------------------------------------
        {%- if cookiecutter.python_version_3 %}
            {%- set run_python_version = 3 %}
        {%- else %}
            {%- set run_python_version = 2 %}
        {%- endif %}
    if version_info < {{ run_python_version }}:
        raise RuntimeError("You need Python {{ run_python_version }}.x or higher to run {{ cookiecutter.tool_name }}")
    {%- endif %}

    # --------------------------------------------------------------------------
    # INSERT YOUR CODE HERE  # TODO
    # --------------------------------------------------------------------------