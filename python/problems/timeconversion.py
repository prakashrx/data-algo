#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s: str):
    # Write your code here
    hh = int(s[:2])
    if s[-2:] == 'PM':
        return f'{(hh % 12) + 12:02d}{s[2:-2]}'
    return f'{hh % 12:02d}{s[2:-2]}'


print(timeConversion('12:00:00PM'))
