#!/usr/bin/env python3
import sys

""" slicing strings = my_string[start:stop:step]
[1:] = start from the second word forward
[2:5] = start on position 2 and end in 4 (5 not included) """
param = sys.argv[1:]

if len(param) == 0:
    print("none")
else:
	print(f"parameters: {len(param)}")
	for string in param:
		print(f"{string}: {len(string)}")
