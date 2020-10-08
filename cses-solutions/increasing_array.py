import sys
import re
import math
from collections import *
 
n = int(input())
l = list(map(int, input().strip().split()))
 
c = 0
for i in range(len(l)-1):
    if l[i+1] < l[i]:
        temp = abs(l[i+1]-l[i])
        c+=temp
	l[i+1] = l[i]
print(c)
