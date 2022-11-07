#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    unsorted = arr[n-1]
    index = n - 1
    while index >= 0:
        if unsorted < arr[index - 1] and index != 0:
            arr[index] = arr[index - 1]
            print(" ".join(map(str, arr)))
        else:
            arr[index] = unsorted
            print(" ".join(map(str, arr)))
            break
        index -= 1



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
