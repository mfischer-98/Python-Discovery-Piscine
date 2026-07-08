#!/usr/bin/env python3
import sys

param = sys.argv[1:]
# slicing strings = my_string[start:stop:step]
# [1:] = start from the second word forward
# [2:5] = start on position 2 and end in 4 (5 not included)

if len(param) == 1:
    print("none")
else:
	print(f"parameters: {len(param)}")
	for string in param:
		print(f"{string}: {len(string)}")