#!/usr/bin/env python3
import sys

param = sys.argv

if len(param) != 3:
	print("none")
else:
	num1 = int(param[1])
	num2 = int(param[2])
	if (num1 >= num2):
		print("First number has to be smaller than second")
	else:
		print(list(range(num1, num2 + 1)))
	