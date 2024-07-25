#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    nom = 0
    denom = (a+1) * (b+1)
    for i in range(0, a+1):
        for j in range(0, b+1):
            if i + j < c:
                nom+=1
    if nom == denom:
        return str(1)
    if nom == 0:
        return str(0)
    print(str(nom))
    print(str(denom))
    com = math.gcd(nom, denom)
    nom = nom / com
    denom = denom / com
    return f"{nom}/{denom}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
    print(result)
