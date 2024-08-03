#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    freqs = []
    mostfreq = 0
    co = Counter(arr)
    freqs = co.most_common()
    for i in range(1, len(arr)):
        if freqs[i-1][1] == freqs[i][1]:
            return min(freqs[i-1][0], freqs[i][0])
        else:
            return freqs[0][0]
    

    #for i in range(1, len(arr)):
     #   if Counter(arr).most_common()[i][1] == Counter(arr).most_common()[i -1][1]:
      #      return min(Counter(arr).most_common()[i][0])
       # mostfreq = Counter(arr).most_common()[0][0]
        #return mostfreq
            
            
    
    return mostfreq
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
