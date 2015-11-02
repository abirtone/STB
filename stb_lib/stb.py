# -*- coding: utf-8 -*-


import six
import argparse

from termcolor import colored


# ----------------------------------------------------------------------
def banner():
    _banner = '''
   _____ _______ ____
  / ____|__   __|  _ \\
 | (___    | |  | |_) |
  \___ \   | |  |  _ <
  ____) |  | |  | |_) |
 |_____/   |_|  |____/

 %s %s %s
 ''' % (colored("Security", "red"),
        colored("Tool", "blue"),
        colored("Builder", "yellow"))

    return _banner


# ----------------------------------------------------------------------
def main():
    from .api import run_console, GlobalParameters

    examples = '''
Examples:

    * Launch wizard and save project in current location:
        %(tool_name)s
    * Launch wizard and save project in /home/new_project
        %(tool_name)s -o /home/new_project
    '''  % dict(tool_name="stb")

    # parser = argparse.ArgumentParser(description='%s security tool' % "sample".capitalize(), epilog=examples,
    parser = argparse.ArgumentParser(description=banner(), epilog=examples,
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     )

    # Main options
    parser.add_argument("-o", "--out-put", dest="output", help="output dir where store project", default=".")

    parsed_args = parser.parse_args()

    # Set Global Config
    config = GlobalParameters(parsed_args)

    # Display banner
    six.print_(banner())

    run_console(config)
    try:
        pass
    except KeyboardInterrupt:
        log.warning("[*] CTRL+C caught. Exiting...")
    except Exception as e:
        print(e)
        log.info("[!] Unhandled exception: %s" % str(e))

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
    import stb_lib
    __package__ = str("stb_lib")

    del sys, os

    main()