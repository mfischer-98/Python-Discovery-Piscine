#!/usr/bin/env python3
import sys
import re

param = sys.argv

if len(param) != 3:
    print("none")
else:
    result = re.findall(param[1],param[2])
    if len(result) > 0:
        print(len(result))
    else:
        print("none")
