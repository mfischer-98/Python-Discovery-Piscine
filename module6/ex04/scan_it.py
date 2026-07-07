#!/usr/bin/env python3
import sys
import re

param = sys.argv

if len(param) != 3:
    print("none")
else:
    result = re.findall(param[1],param[2])
    print(len(result))
