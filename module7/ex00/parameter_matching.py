#!/usr/bin/env python3
import sys

param = sys.argv
if len(param) != 2:
	print("none")
else:
	guess = input("What was the parameter? ")
	if param[1] == guess:
		print("Good job!")
	else:
		print("Nope, sorry...")
