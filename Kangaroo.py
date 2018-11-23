#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    tFloat = 1.00*(x2-x1)/(v1-v2)
    tInt = (x2-x1)//(v1-v2)
    if tInt > 0 and tInt == tFloat:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    # fptr = open("solution.txt", 'w+')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print result
    # fptr.write(result + '\n')

    # fptr.close()
