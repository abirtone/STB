# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import join, abspath, dirname
from cookiecutter.main import cookiecutter


# ----------------------------------------------------------------------
def build_project(config, responses):
    """
    :param config: GlobalParameters option instance
    :type config: `GlobalParameters`

    :param responses: dict with responses of wizard
    :type responses: dict(str->*)
    
    """
    # Add datetime
    responses["today_year"] = datetime.now().strftime("%Y")

    path = join(abspath(dirname(__file__)), "..", "resources/cookiecutter-security-tool-template")

    cookiecutter(path,
                 extra_context=responses,
                 no_input=True)
