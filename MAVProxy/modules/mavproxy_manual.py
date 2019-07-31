#!/usr/bin/env python
'''reset Pixhawk command'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil

class ManualModule(mp_module.MPModule):
	def __init__(self, mpstate):
		super(ManualModule, self).__init__(mpstate, "manual", "manual commands")
		self.add_command('manual', self.cmd_manual, "Shows help options")
		self.add_command('left', self.cmd_l, "Go left")
		self.add_command('right', self.cmd_r, "Go right")
		self.add_command('up', self.cmd_u, "Go up")
		self.add_command('down', self.cmd_d, "Go down")
		self.add_command('forward', self.cmd_f, "Go forward")
		self.add_command('backward', self.cmd_b, "Go backward")
		self.add_command('clockwise', self.cmd_cl, "Turns clockwise")
		self.add_command('counter', self.cmd_cc, "Turns counter clockwise")
		self.add_command("line", self.cmd_fb, "Moves ROV forward then back")
		self.add_command("script", self.cmd_script, "Moves ROV in square")

	def usage(self):
		'''show help on command line options'''
		return "Usage: left, right, up, down, forward, backward, clockwise, counter (counter clockwise), line, script."

	def cmd_manual(self,args):
		if len(args) == 0:
			print(self.usage())

	"""Send manual command to move ROV up."""
	# XYR on range -1000 - 1000. Z on range 0 - 1000.
	# Max forward speed 1.5 m/s.
	def cmd_u(self,args):
		x = 0
		while x < 4:
			self.master.mav.manual_control_send(self.target_system,
					0, # x, forward/backward
					0, # y, left/right 
					700, # z, thrust
					0, # r, yaw
					0 #button
					)
			time.sleep(.5)
			x += 1
		print("up ✓")

		"""Send manual command to move ROV down about 3 feet."""
	def cmd_d(self,args):
		x = 0
		while x < 4:
			self.master.mav.manual_control_send(self.target_system, 0, 0, 300, 0, 0)
			x += 1
			time.sleep(.5)
		print("down ✓")

	"""Send manual command to move ROV left 3 feet."""
	def cmd_l(self,args):
		x = 0
		while x < 2:
			self.master.mav.manual_control_send(self.target_system,0,-300,500,0, 0)
			time.sleep(.5)
			x += 1
		print("left ✓")

	"""Send manual command to move ROV right about 3 feet."""
	def cmd_r(self, args):
		x = 0
		while x <2:
			self.master.mav.manual_control_send(self.target_system,0, 300,500, 0, 0)
			x +=1
			time.sleep(.5)
		print("right ✓")

	def cmd_f(self,args):
		# x = 0
		# while x < 1:
		self.master.mav.manual_control_send(self.target_system,600, 0, 500, 0, 0)
		# x += 1
		time.sleep(6)
		print("forward ✓")


	"""Send manual command to move ROV backward about 6 feet."""
	def cmd_b(self,args):
		# x = 0
		# while x < 4:
		self.master.mav.manual_control_send(self.target_system,-600, 0, 500, 0,0)
		# x += 1
		time.sleep(6)
		print("backward ✓")

	"""Send manual command to turn ROV clockwise 90°."""
	def cmd_cc(self,args):
		# x =0
		# while x < 4:
		self.master.mav.manual_control_send(self.target_system, 0, 0, 500, -300, 0)
			# x +=1
		time.sleep(6)
		print("counter clockwise ✓")

	"""Send manual command to turn ROV counter clockwise 90°"""
	def cmd_cl(self,args):
		# x = 0
		# while x < 4:
		self.master.mav.manual_control_send(self.target_system, 0, 0, 500, 300, 0)
			# x += 1
		time.sleep(6)
		print("clockwise ✓")

	"""Moves ROV forward about 6 feet waits for 10 seconds and back about 6 feet."""
	def cmd_fb(self,args):
		self.cmd_b(args)
		self.cmd_f(args)

	"""Moves ROV forward about 6 feet, waits for 10 seconds, turns ROV 180 degrees, and moves forward again 6 feet."""
	def cmd_script(self,args):
		self.cmd_f(args)
		time.sleep(10)

		x = 0
		while x < 10:
			self.master.mav.manual_control_send(self.target_system, 0, 0, 500, 90, 0)
			x += 1
			time.sleep(.5)
		print("clockwise ✓")

		time.sleep(10)
		self.cmd_f(args)

def init(mpstate):
	'''initialise module'''
	return ManualModule(mpstate)


