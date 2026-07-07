#!/usr/bin/env python3
import sys

param = sys.argv

if len(param) != 2:
    print("none")
else:
    print(param[1].lower())