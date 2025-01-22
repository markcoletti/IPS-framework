#!/usr/bin/env python3
""" Component wrapper for the ensemble example for `another_sim`. """
from ipsframework import Component


class a_sim_comp(Component):
    def __init__(self, services, config):
        super().__init__(services, config)
        print('Created %s' % (self.__class__))

    def step(self, timestamp=0.0):
        # TODO echo parameters for this run
        print('Hello from another_sim_comp')

        # Echo the parameters we're expecting, D, B, and F
        D = self.services.get_config_param('D')
        B = self.services.get_config_param('B')
        F = self.services.get_config_param('F')

        print(f'a_sim_comp parameters: D={D}, B={B}, F={F}')