# -*- coding: utf-8 -*-

import yaml
import six.moves
import collections

from os.path import abspath, dirname, join
from termcolor import colored


# ----------------------------------------------------------------------
def _load_questions():
    """
    Load questions stored in questions.yaml file and return
    """
    # --------------------------------------------------------------------------
    # This code force YAML lib to load entries as OrderedDict
    # --------------------------------------------------------------------------
    _mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG
    
    def dict_representer(dumper, data):
        return dumper.represent_dict(data.iteritems())

    def dict_constructor(loader, node):
        return collections.OrderedDict(loader.construct_pairs(node))

    yaml.add_representer(collections.OrderedDict, dict_representer)
    yaml.add_constructor(_mapping_tag, dict_constructor)

    path = join(abspath(dirname(__file__)), "..", "questions.yaml")

    with open(path, "rU") as f:
        return yaml.load(f.read())


# ----------------------------------------------------------------------
def do_wizard():
    """
    Launch a wizard to request all parameters.

    :return: responses as a dictionary
    :rtype: dict(str->*)

    """
    six.print_("%s Requesting queries needed to build project:" % colored("[*]", "blue"))

    # Load questions
    questions = _load_questions()

    # Get responses
    responses = {}
    for var, prop in six.iteritems(questions):

        # Properties
        prop_type = prop.get('type', 'int')
        mandatory = prop.get('mandatory', False)
        default = prop.get('default', "")
        label = prop.get('label', "").strip()

        if not label:
            continue

        # Build message
        msg = "    %s %s" % (colored("<i>", "yellow"), label)

        # Is mandatory?
        if default and not mandatory:
            msg += " (%s)" % default

        # Add ":" end
        msg += ": "

        # Ask
        while 1:
            _tmp_res = six.moves.input(msg)

            # Empty answer allowed?
            if not _tmp_res:
                if mandatory:
                    six.moves.input("    %s %s" % (colored("<!>", "red"), "This question is mandatory."))
                    continue

                if default:
                    _tmp_res = default

            _tmp_res = _tmp_res.strip()

            # Check answer type
            if prop_type == "int":
                try:
                    _tmp_res = int(_tmp_res)
                except ValueError:
                    six.moves.input("    %s %s" % (colored("<!>", "red"), "This question must be answered with a number."))
                    continue
            elif prop_type == "bool":
                if _tmp_res not in ("yes", "y", "no", "n"):
                    six.moves.input("    %s %s" % (colored("<!>", "red"),
                                             "This question must be answered with 'yes/no' or 'y/n'."))
                    continue
            elif prop_type == "str":
                pass

            # Store information and exit
            responses[var] = _tmp_res
            break

    return responses
