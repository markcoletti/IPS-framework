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

        # Get the template input file
        ports = self.services.get_global_param('PORTS')
        component = ['WORKER']

        # Specifies three sets of variable values for three
        # concurrent ensemble runs of the WORKER component.
        variables = [{‘A’: 3, ‘B’: 2.34, ‘C’: ‘bar’},
        {‘A’: 2, ‘B’: 5.82, ‘C’: ‘baz’},
        {‘A’: 4, ‘B’: 0.1, ‘C’: ‘quux’}]

        # spins up N tasks, in this case 3, each with a different set of
        # variable values
        self.services.run_ensemble(component, ensemble_variables)
