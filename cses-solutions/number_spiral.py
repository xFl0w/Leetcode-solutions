import sys
import re
import math
from collections import *

n = int(input())

while n > 0:
    y, x = list(map(int, input().strip().split()))
    if x > y:
        if x%2 == 1:
            print(x*x-y+1)
        else:
            x-=1
            print(x*x+y)
    else:
        if y%2 == 0:
            print(y*y-x+1)
        else:
            y-=1
            print(y*y+x)
    n-=1
