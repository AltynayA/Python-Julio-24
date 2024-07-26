#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    stair = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n - i -1):
            stair[i][j] = " "
        for j in range(n-i-1, n):
            stair[i][j] = "#"
    for i in range(n):
        print("".join(str(x) for x in stair[i]))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
