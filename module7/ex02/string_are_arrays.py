#!/usr/bin/env python3
import sys

param = sys.argv
flag = 0

if len(param) != 2:
	print("none")
else:
	for c in param[1]:
		if c == 'z':
			print("z", end='')
			flag = 1
	if flag == 0:
		print("none")
	else:
		print("")