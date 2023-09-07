class Solution:

	""" 4. Median of Two Sorted Arrays """

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

		""" O(m+n) solution """

		mergedList = []
		len1 = len(nums1)
		len2 = len(nums2)
		length = len1 + len2

		if nums1 and nums2:

			index1 = 0
			index2 = 0

			for i in range(length):
				if index1 < len1 and index2 < len2:
					if nums1[index1] < nums2[index2]:
						mergedList.append(nums1[index1])
						index1 = index1 + 1
					else:
						mergedList.append(nums2[index2])
						index2 = index2 + 1
				elif index1 < len1:
					mergedList = mergedList + nums1[index1:]
				elif index2 < len2:
					mergedList = mergedList + nums2[index2:]

			nums1 = []
			nums2 = []
			
			if length % 2 == 0:
				return 0.5*(mergedList[length//2-1] + mergedList[length//2])
			else:
				return mergedList[length//2]
		
		elif nums1:

			if length % 2 == 0:
				return 0.5*(nums1[length//2-1] + nums1[length//2])
			else:
				return nums1[length//2]	  

		elif nums2:

			if length % 2 == 0:
				return 0.5*(nums2[length//2-1] + nums2[length//2])
			else:
				return nums2[length//2]

	def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:

		""" O(log(m+n)) solution """

		
