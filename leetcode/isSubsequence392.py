class Solution:

	""" 392. Is Subsequence """

	def isSubsequence(self, s: str, t: str) -> bool:
		
		index = 0
	
		if not s:
			return True
	
		for char in t:
			if char == s[index]:
				index = index + 1
			if index == len(s):
				return True
	
		return False
