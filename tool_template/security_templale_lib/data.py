#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
This file contains main data structures of proyect
"""

import six


# --------------------------------------------------------------------------
class GlobalParameters:
    """Global parameters of proyect"""

    # ----------------------------------------------------------------------
    def __init__(self, from_argparse=None, **kwargs):  # TODO
        """
        Setup parameters from argparser of option by option
        """

        # Auto set config from argparser
        if from_argparse is not None:
            from argparse import Namespace
            if isinstance(from_argparse, Namespace):
                for p_name, p_value in six.iteritems(vars(from_argparse)):
                    setattr(self, p_name, p_value)
