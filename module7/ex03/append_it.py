#!/usr/bin/env python3
import sys

param = sys.argv[1:]

if len(param) < 1:
	print("none")
else:
	for word in param:
		if word.find("ism", len(word) - 3) == -1:
			print(word + "ism")
