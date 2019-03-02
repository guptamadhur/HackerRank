# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Hacker Rank Practice Python

import math
import os
import random
import re
import sys
import datetime
from dateutil.parser import parse

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt = parse(t1) - parse(t2)
    return str(abs(int(dt.total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()