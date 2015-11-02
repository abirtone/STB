# -*- coding: utf-8 -*-


"""
This file contains main data structures of project
"""

import six

from os.path import abspath, dirname


# --------------------------------------------------------------------------
class GlobalParameters:
    """Global parameters of project"""

    # ----------------------------------------------------------------------
    def __init__(self, from_argparse=None, **kwargs):
        """
        Setup parameters from argparser of option by option
        """

        # Auto set config from argparser
        if from_argparse is not None:
            from argparse import Namespace
            if isinstance(from_argparse, Namespace):
                for p_name, p_value in six.iteritems(vars(from_argparse)):
                    setattr(self, p_name, p_value)

        # Fix output dir
        self.output = abspath(dirname(self.output))
