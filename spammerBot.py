import pyautogui as gui
import time
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('-f', type=str, required=True, help="specify input file")

# Parse the argument
args = parser.parse_args()
time.sleep(5)
file = open(args.f,'r')
for line in file:
	gui.typewrite(line)
	gui.press('enter')