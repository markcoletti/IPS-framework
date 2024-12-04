#!/usr/bin/env python3
"""
    Example driver for the ensembles example
"""
import os
from ipsframework import Component

class ensemble_driver(Component):

    def __init__(self):
        super().__init__(services, config)

    def step(self, timestamp=0.0, **keywords):
        """ set up and run the ensemble
        """
        self.services.stage_state()

        # Define dict of ensemble variables
        ensemble_variables = {
            'X0': [1, 2, 3, 4, 5],
            'a_line': [2.34, 5.82, 0.1],
            'foo': ['bar', 'baz', 'qux']
            # will have other means of creating ranges; e.g., generator functions
        }

        # Get the template input file
        ports = self.services.get_global_param('PORTS')
        template = ['ENSEMBLE']['TEMPLATE']

        # `excludes` is a callback function that will be called for each
        # ensemble member. If it returns True, the ensemble member will be
        # excluded from the ensemble.  This is a way for a SME to filter out
        # combinations that are not valid.
        self.services.run_ensemble(template, ensemble_variables, excludes=None)