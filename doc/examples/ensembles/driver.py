#!/usr/bin/env python3
"""
    Example driver for the ensembles example.

    Please note that run_ensemble can be run from any IPS component, not
    just a driver. The driver is used here for simplicity.
"""
from pathlib import Path

from ipsframework import Component


class ensemble_driver(Component):

    def __init__(self, services, config):
        super().__init__(services, config)
        print('Creating driver')

    def init(self, timeStamp=0.0):
        return

    def step(self, timestamp=0.0, **keywords):
        """ set up and run the ensemble
        """
        # ENSEMBLE_DIR is an arbitrary variable denoting where we want to run
        # all the ensembles.  You don't have to use ENSEMBLE_DIR. You can
        # even hardcode the path here.  Whatever.
        run_dir = Path(self.services.get_config_param('ENSEMBLE_DIR'))
        print(f'Running ensemble in {run_dir}')

        template = self.config['TEMPLATE']
        print(f'Using template {template}')

        # PLATFORM_CONFIG_FILE is a variable that points to the platform
        # config file used by the ensembles.  This could be the same
        # platform config file used for this driver, but it doesn't have to be.
        platform_config = self.config['PLATFORM_CONFIG_FILE']

        # Specifies different sets of variable values for concurrent ensemble
        # runs for two different components, 'A_SIM_COMP' and
        # 'ANOTHER_SIM_COMP', that correspond to two different coupled
        # simulations.  We chose two components to demonstrate that the same
        # variable, in this case 'B', can have different values for different
        # components. Moreover, this example shows that the different
        # components needn't have the same number of variable values,
        # but those within each component there should be the same number.
        # E.g., 'A_SIM_COMP' has 3 values for 'A', 'B', and 'C', while
        # 'ANOTHER_SIM_COMP' has 2 values for 'D', 'B', and 'F'.
        # 'A_SIM_COMP' and 'ANOTHER_SIM_COMP' are the names of the config
        # sections in the template file so we know where to look for
        # variable substitutions.
        variables = {'A_SIM_COMP': {'A': [3, 2, 4],
                                    'B': [2.34, 5.82, 0.1],
                                    'C': ['bar', 'baz', 'quux']},
                     'ANOTHER_SIM_COMP': {'D': [7, 5, 9],
                                          'B': [0.775, 0.080, 29.2],
                                          'F': ['xyzzy', 'plud', 'thud']}}

        # Spins up N tasks, in this case 5 (3 for a_sim and 2 for blue),
        # each with a different set of variable values. `mapping` is a dict
        # that maps the specific simulation to a given run directory so that
        # the user can easily find the output for a specific run.
        mapping = self.services.run_ensemble(template,
                                             variables,
                                             run_dir,
                                             platform_config)

        print(f'Mapping of dirs to parameters: {mapping!s}')


    def finalize(self, timeStamp=0.0):
        return

