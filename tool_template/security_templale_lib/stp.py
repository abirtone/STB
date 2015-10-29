#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging

log = logging.getLogger(__name__)


# ----------------------------------------------------------------------
def main():

    from .api import run_console, GlobalParameters

    examples = '''
Examples:

    * Scan target using default 50 most common plugins:
        %{tool_name}s TARGET
    '''  # TODO

    parser = argparse.ArgumentParser(description='%{TOOL_NAME}s', epilog=examples,  # TODO
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("target", metavar="TARGET", nargs="*")
    parser.add_argument("-v", "--verbosity", dest="verbose", action="count", help="verbosity level: -v, -vv, -vvv.", default=0)

    parsed_args = parser.parse_args()

    config = GlobalParameters(parsed_args)

    try:
        run_console(config)
    except KeyboardInterrupt:
        log("[*] Exiting ...\n")
    except Exception as e:
        pass

if __name__ == "__main__" and __package__ is None:
    # --------------------------------------------------------------------------
    #
    # INTERNAL USE: DO NOT MODIFY THIS SECTION!!!!!
    #
    # --------------------------------------------------------------------------
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import security_template_lib  # TODO
    __package__ = str("security_templale_lib")  # TODO

    # Check Python version
    # if sys.version_info < (3, 3):
    #     print("\n[!] You need a Python version greater than 3.3\n")
    #     exit(1)
    del sys, os

    main()
