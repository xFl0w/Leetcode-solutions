n = int(input())
 
l = list(map(int, input().strip().split()))
 
l.sort()
 
l1 = []
for i in range(1, n+1):
    l1.append(i)
 
print(*set(l1).difference(set(l)))
