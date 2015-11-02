# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

import six

from termcolor import colored

from .data import *
from .libs.wizard import do_wizard
from .libs.build import build_project

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

    # Launch questions
    responses = do_wizard()

    # Build project
    six.print_(colored("[*]", "blue"), "Building project")
    run(config, responses)
    six.print_(colored("[*]", "blue"), "Done!")


# ----------------------------------------------------------------------
#
# API call
#
# ----------------------------------------------------------------------
def run(config, responses):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :raises: TypeError
    """
    if not isinstance(config, GlobalParameters):
        raise TypeError("Expected GlobalParameters, got '%s' instead" % type(config))

    # Create project
    build_project(config, responses)
