class Solution:
	def buildArray(self, target, n):
		c = 0
		l = []
		for i in range(1, n+1):
			l.append("Push")
			if target[c] == i:
				c+=1
			else:
				l.append("Pop")
			if c == len(target):
				return l
