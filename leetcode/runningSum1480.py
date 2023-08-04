class Solution:

	def runningSum(self, nums: List[int]) -> List[int]:
	
		""" 1480. Running Sum of 1d Array """
	
		rSum = [nums[0]]
		for i in range(1,len(nums)):
			rSum.append(rSum[i-1]+nums[i])
	
		return rSum
