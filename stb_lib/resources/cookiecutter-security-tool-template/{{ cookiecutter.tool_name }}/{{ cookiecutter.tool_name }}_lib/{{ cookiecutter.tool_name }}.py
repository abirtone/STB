# -*- coding: utf-8 -*-

import argparse
import logging

logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger(__name__)


# ----------------------------------------------------------------------
def main():

    from .api import run_console, GlobalParameters

    examples = '''
Examples:

    * Scan target using default 50 most common plugins:
        %(tool_name)s TARGET
    '''  % dict(tool_name="{{ cookiecutter.tool_name|lower|replace(" ", "_") }}")

    parser = argparse.ArgumentParser(description='%s security tool' % "{{ cookiecutter.tool_name }}".capitalize(), epilog=examples,
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("target", metavar="TARGET", nargs="*")
    parser.add_argument("-v", "--verbosity", dest="verbose", action="count", help="verbosity level: -v, -vv, -vvv.",
                        default=1)

    parsed_args = parser.parse_args()

    # Configure global log
    log.setLevel(abs(5 - parsed_args.verbose) % 5)

    # Set Global Config
    config = GlobalParameters(parsed_args)

    try:
        run_console(config)
    except KeyboardInterrupt:
        log.warning("[*] CTRL+C caught. Exiting...")
    except Exception as e:
        log.critical("[!] Unhandled exception: %s" % str(e))

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
    import {{ cookiecutter.tool_name|lower| replace(" ", "_") }}_lib
    __package__ = str("{{ cookiecutter.tool_name }}_lib")

    {%- if cookiecutter.python_version_3 != cookiecutter.python_version_2 %}
    # Checks Python version
    {%- if cookiecutter.python_version_3 %}
    {%- set run_python_version = 3 %}
    {%- else %}
    {%- set run_python_version = 2 %}
    {%- endif %}
    if sys.version_info < {{ run_python_version }}:
        print("\n[!] You need a Python version greater than {{ run_python_version }}.x\n")
        exit(1)
    {%- endif %}

    del sys, os

    main()
