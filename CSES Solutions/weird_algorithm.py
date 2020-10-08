n = int(input())
 
ans = []
ans.append(n)
 
while n > 1:
    if n%2 == 0:
        temp = n//2
	n = temp
	ans.append(temp)
 
    elif n%2 == 1:
	temp = n*3+1
	n = temp
	ans.append(temp)
 
print(*ans)
