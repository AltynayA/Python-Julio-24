#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    s =s.split(':')
    if int(s[0]) == 12:
        if s[len(s) - 1][2] == "P":
            s[0] = "12"
        if s[len(s) - 1][2] == "A":
            s[0] = "00"
    elif s[len(s) - 1][2] == "P":
        if int(s[0]) < 12:
            s[0] = str(int(s[0]) + 12)
    
        
    s[len(s)-1] = s[len(s) -1][0] + s[len(s) -1][1]
    s = ':'.join(s)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    print(result)