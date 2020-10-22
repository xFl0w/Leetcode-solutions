class Solution:
	def maxDepth(self, s):
		l, c = 0, 0
		for i in s:
			if i == '(':
				l+=1
				c = max(l, c)
			elif i == ')':
				l-=1
		return c
