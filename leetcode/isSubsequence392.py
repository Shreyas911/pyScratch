class Solution:

	def isSubsequence(self, s: str, t: str) -> bool:
	
		""" 392. Is Subsequence """
	
		index = 0
	
		if not s:
			return True
	
		for char in t:
			if char == s[index]:
				index = index + 1
			if index == len(s):
				return True
	
		return False
