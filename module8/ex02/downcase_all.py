#!/usr/bin/env python3
import sys

def downcase_it(text):
	return text.lower()

args = sys.argv[1:]

if len(args) < 1:
	print("none")

for word in args:
	print(downcase_it(word))