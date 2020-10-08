class Solution:
	def minSubsequence(self, nums):
		ans = []
		nums.sort(reverse=True)
		c = 0
		t = sum(nums)
		for i in nums:
			t -= i
			c += i
			ans.append(i)
			if c > t:
				break
		return ans
