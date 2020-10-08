import sys
import re
import math
from collections import *
 
s = str(input())
ans = 0
r = r'(.)\1+'
mx = sorted((m.group() for m in re.finditer(r, s)))
for i in mx:
	temp = len(i)
	ans = max(temp, ans)
if ans == 0:
	ans+=1
print(ans)
