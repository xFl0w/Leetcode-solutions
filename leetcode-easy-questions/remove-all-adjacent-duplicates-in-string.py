class Solution:
	def removeDuplicates(self, S):
		l = []
		for i in S:
			if len(l) == 0:
				l.append(i)
			else:
				temp = l[len(l)-1]
				if i == temp:
					l.pop()
				else:
					l.append(i)
		return "".join(l)
