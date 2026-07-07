#!/usr/bin/env python3
import sys

param = sys.argv

if len(param) < 3:
    print("none")
else:
    param.remove("./aff_rev_params.py")
    for string in reversed(param):
        print(string)
