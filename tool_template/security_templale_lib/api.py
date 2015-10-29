# -*- coding: utf-8 -*-

"""
This file contains API calls and Data
"""

from .data import *

__version__ = "1.0.0"
__all__ = ["run_console", "GlobalParameters"]


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

    # --------------------------------------------------------------------------
    # Checks Python version
    # --------------------------------------------------------------------------
    # if version_info < (3, 3):
    #     raise RuntimeError("You need Python 3.3.x or higher to run %{TOOL_NAME}s")

    # TODO