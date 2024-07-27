#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for num in arr:
        if num != 0:
            if num < 0:
                neg+= 1
            else:
                pos+=1
        else:
            zer+=1
    pos = pos/len(arr)
    neg = neg/len(arr)
    zer = zer/len(arr)
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zer))
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
