#!/usr/bin/env python3
"""
    Example driver for the ensembles example.

    Please note that run_ensemble can be run from any IPS component, not
    just a driver. The driver is used here for simplicity.
"""
import os
from timeit import template

from ipsframework import Component


class ensemble_driver(Component):

    def __init__(self, services, config):
        super().__init__(services, config)

    def step(self, timestamp=0.0, **keywords):
        """ set up and run the ensemble
        """
        run_dir = self.config.get_global_param(self, self.services, 'ENSEMBLE_DIR')

        template = self.config.get_config_param('driver.TEMPLATE')

        # Specifies three sets of variable values for three
        # concurrent ensemble runs of the WORKER component.
        variables = {'orange': {'A': [3, 2, 4],'B': [2.34, 5.82, 0.1],'C': ['bar', 'baz', 'quux']},
                     'blue'  : {'A': [3, 2, 4],'B': [2.34, 5.82, 0.1],'C': ['bar', 'baz', 'quux']} }

        # spins up N tasks, in this case 3, each with a different set of
        # variable values
        self.services.run_ensemble(template, variables, run_dir)
