#!/usr/bin/env python3
import sys

def shrink(text):
	print(text[:8])

def enlarge(text):
	while len(text) < 8:
		text += 'Z'
	print(text)

param = sys.argv[1:]

if len(param) == 0:
	print("none")
else:
	for word in param:
		if len(word) > 8:
			shrink(word)
		elif len(word) < 8:
			enlarge(word)
		else:
			print(word)