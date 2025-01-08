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
        # ENSEMBLE_DIR is an arbitrary variable denoting where we want to run
        # all the ensembles.
        run_dir = self.config.get_global_param(self, self.services,
                                               'ENSEMBLE_DIR')

        template = self.config.get_config_param('TEMPLATE')

        # Specifies different sets of variable values for concurrent ensemble
        # runs for two different components, 'a_sim' and 'another_sim',
        # that correspond to two different coupled simulations.  We chose two
        # components to demonstrate that the same variable, in this case 'B',
        # can have different values for different components. Moreover,
        # this example shows that the different components needn't have the
        # same number of variable values, but those within each component
        # there should be the same number.  E.g., 'a_sim' has 3 values for
        # 'A', 'B', and 'C', while 'another_sim' has 2 values for 'D', 'B', and 'F'.
        variables = {'a_sim': {'A': [3, 2, 4],
                                'B': [2.34, 5.82, 0.1],
                                'C': ['bar', 'baz', 'quux']},
                     'another_sim': {'D': [7, 5],
                                'B': [0.775, 0.080],
                                'F': ['xyzzy', 'plud']} }

        # Spins up N tasks, in this case 5 (3 for a_sim and 2 for blue),
        # each with a different set of variable values.
        # self.services.run_ensemble(template, variables, run_dir)
