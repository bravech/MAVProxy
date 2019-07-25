#!/usr/bin/env python
'''reset Pixhawk command'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil

class ResetModule(mp_module.MPModule):
	def __init__(self, mpstate):
		super(ResetModule, self).__init__(mpstate, "reset", "reset module")
		self.add_command('Reset', self.cmd_reset, "reset the pixhawk")
		self.add_command('resett', self.cmd_resett, "Shows help options")

	def usage(self):
		'''show help on command line options'''
		return "Usage: Reset"

	def cmd_resett(self,args):
		if len(args) == 0:
			print(self.usage())

	def cmd_reset(self, args):
		'''sends a reboot command'''
		self.master.mav.command_long_send(
				self.target_system,  # target_system
				self.target_component,
				mavutil.mavlink.MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN, # command
				0, # confirmation
				1, # param1 (reboot pixhawk)
				0, # param2 (0: Do nothing for onboard computer)
				0, # param3 (0: Do nothing for camera)
				0, # param4 (0: Do nothing for mount )
				0, # param5 (Reserved)
				0, # param6 (Reserved)
				0) # param7 (ID (e.g. camera ID -1 for all IDs))
		print("Pixhawk rebooted. Wait for reconnection.")


def init(mpstate):
	'''initialise module'''
	return ResetModule(mpstate)


