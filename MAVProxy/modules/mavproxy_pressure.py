#!/usr/bin/env python
'''Pressure module'''

import time, math
from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

class PressureModule(mp_module.MPModule):
	def __init__(self, mpstate):
		super(PressureModule, self).__init__(mpstate, "Pressure", "pressure module")
		'''initialisation code'''
		self.add_command('press', self.cmd_press, "show pressure information")
		self.add_command('press_cal', self.cmd_press_cal, "callibrate")
		self.add_command('pressure', self.cmd_pressure, "shows help information")
		self.console.set_status('Pressure', 'Pressure ---', row=2)
		self.abspress = -1
		self.surf_pressure = 1013.25
		self.press_cal = -1
		self.depth = 0


	def usage(self):
		'''show help on command line options'''
		return "Usage: press, press_cal."

	def cmd_pressure(self,args):
		if len(args) == 0:
			print(self.usage())

	def cmd_press(self, args):
		'''show battery levels'''
		print("Absolute Pressure:   %.1f mbar" % self.abspress)
		print("Depth: %.1f feet" % self.depth)
		

	def pressure_update(self, SCALED_PRESSURE):
		"""Updates pressure"""
		self.abspress = SCALED_PRESSURE.press_abs
		self.press_cal = self.abspress - self.surf_pressure
		self.depth = self.press_cal * 0.033455256555148


	def report_pressure(self):
		pressure_string = 'RawPress: %.1f mb   CalPress: %.1f mb   Depth: %.1f ft' % (self.abspress, self.press_cal, self.depth)
		self.console.set_status('Alt', pressure_string, row=2)
		

	def mavlink_packet(self, m):
		'''handle a mavlink packet'''
		mtype = m.get_type()
		if mtype == "SCALED_PRESSURE2":
			self.pressure_update(m)
			self.report_pressure()

	def cmd_press_cal(self, args):
		self.surf_pressure = self.abspress



def init(mpstate):
	'''initialise module'''
	return PressureModule(mpstate)