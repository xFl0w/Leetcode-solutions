from collections import *
class Solution:
	def sortArrayByParityII(self, A):
		dd = defaultdict(list)
		for i in A:
			if i%2 == 0:
				dd['even'].append(i)
			else:
				dd['odd'].append(i)
		for i in range(len(A)):
			if i%2 == 0:
				A[i] = dd['even'].pop()
			else:
				A[i] = dd['odd'].pop()
		return A
