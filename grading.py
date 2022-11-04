#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded = []
    for grade in grades:
        if grade < 38 or grade == 100:
            rounded.append(grade)
        else:
            last = grade % 10
            first = grade // 10
            if last > 7:
                grade = (first + 1) * 10
                rounded.append(grade)
            elif 2 < last < 5:
                grade = (first * 10) + 5
                rounded.append(grade)
            else:
                rounded.append(grade)
    return rounded



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
