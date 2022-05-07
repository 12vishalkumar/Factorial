import math
import os
import random
import re
import sys

# Complete the 'extraLongFactorials' function below.
# The function accepts INTEGER n as parameter.

def extraLongFactorials(n):
    # Write your code here
    fect = 1
    for i in range(n, 0, -1):
        fect *= i
    print(fect)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)