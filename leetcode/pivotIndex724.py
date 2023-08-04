class Solution:

	""" 724. Find Pivot Index """

	def pivotIndex(self, nums: List[int]) -> int:
	
		leftSum = 0
		rightSum = sum(nums[1:])
	
		if leftSum == rightSum:
			return 0
	
		for i in range(1,len(nums)):
			leftSum = leftSum+nums[i-1]
			rightSum = rightSum-nums[i]
	
			if leftSum == rightSum:
				return i
		
		return -1
