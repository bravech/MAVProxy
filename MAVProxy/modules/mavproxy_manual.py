#!/usr/bin/env python
'''reset Pixhawk command'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil
import sys, termios, tty

class ManualModule(mp_module.MPModule):
	def __init__(self, mpstate):
		super(ManualModule, self).__init__(mpstate, "manual", "manual commands")
		self.add_command('left', self.cmd_l, "Go left")
		self.add_command('right', self.cmd_r, "Go right")
		self.add_command('up', self.cmd_u, "Go up")
		self.add_command('down', self.cmd_d, "Go down")
		self.add_command('forward', self.cmd_f, "Go forward")
		self.add_command('backward', self.cmd_b, "Go backward")
		self.add_command('clockwise', self.cmd_cl, "Turns clockwise")
		self.add_command('counter clockwise', self.cmd_cc, "Turns counter clockwise")
		self.add_command("test", self.cmd_test, "test")


	"""Allows keyboard input."""
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
		return ch

	"""Send manual command to move ROV left."""
	def cmd_l(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					-500, # y
					500, # z
					0, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to move ROV right."""
	def cmd_r(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					500, # y
					500, # z
					0, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to move ROV up."""
	def cmd_u(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					0, # y
					750, # z
					0, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to move ROV down."""
	def cmd_d(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					0, # y
					250, # z
					0, # r
					0 #button 
					)
			if (char == "s"):
				break

	"""Send manual command to move ROV forward."""
	def cmd_f(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					500, # x
					0, # y
					500, # z
					0, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to move ROV backward."""
	def cmd_b(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					-500, # x
					0, # y
					500, # z
					0, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to turn ROV clockwise."""
	def cmd_cl(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					0, # y
					500, # z
					-500, # r
					0 #button
					)
			if (char == "s"):
				break

	"""Send manual command to turn ROV counter clockwise."""
	def cmd_cc(self, args):
		char = getch()
		while True:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					0, # y
					500, # z
					500, # r
					0 #button
					)
			if (char == "s"):
				break

	def cmd_test(self,args):
		char = getch()
		x = 0
		while x < 10:
			self.master.mav.manual_control_send(connection.target_system,
					0, # x
					0, # y
					500, # z
					500, # r
					0 #button
					)
			x += 1
			if (char == "s"):
				break

def init(mpstate):
	'''initialise module'''
	return ManualModule(mpstate)


