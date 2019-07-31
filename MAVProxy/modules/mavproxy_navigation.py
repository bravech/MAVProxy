 #!/usr/bin/env python
'''Custom Navigation Command With Duration'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil
import sys, traceback

class CustomModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(CustomModule, self).__init__(mpstate, "navigation", "navigation")
        self.add_command('test', self.cmd_test, "Testing the nav commands")
        '''initialisation code'''

    def cmd_test(self, args):
        self.master.mav.manual_control_duration_send(self.target_system,
            0,
            0,
            500,
            0,
            0,
            1123)

    def mavlink_packet(self, m):
        'handle a mavlink packet'''
        if m.get_type() == 'MANUAL_CONTROL_DURATION':
            os.system("wall" + " control duration recv'd: " + "x: " + str(m.x) + "dur: " + str(m.duration))

def init(mpstate):
    '''initialise module'''
    return CustomModule(mpstate)