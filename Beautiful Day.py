import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.(My part)
def beautifulDays(i, j, k):
    return(len([_ for _ in range(i,j+1) if (_ - int(str(_)[::-1]))%k == 0 ]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()