from collections import *
class Solution:
	def subdomainVisits(self, cpdomains):
		c = Counter()
		for i in cpdomains:
			count, domain = i.split()
			c[domain] += int(count)
			for i, v in enumerate(domain):
				if v == '.':
					c[domain[i+1:]] += int(count)
		return [str(count)+' '+domain for domain, count in c.items()]
