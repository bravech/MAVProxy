import sys
import termios, tty

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch

char = getch()

if char == "l":
	print("lllllllllllll")

if char == "m":
	print("mmmmmmmmmmmm")