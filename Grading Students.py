#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def roundOff(marks):
    nextMultiple = (marks//5)*5
    if marks < 38:
        return marks
    if marks%5 != 0 and marks >= 38:
        nextMultiple = marks - marks%5 + 5
    else:
        pass

    if (nextMultiple-marks) < 3:
        return nextMultiple
    else:
        return marks

def gradingStudents(grades):
    #
    # Write your code here.
    #
    result = []
    for i in range(0,len(grades)):

        result.append(roundOff(grades[i]))
    return result

if __name__ == '__main__':
    f = open("solution.txt","w+")

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
