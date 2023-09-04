class Solution:

	""" 205. Isomorphic Strings """

	def isIsomorphic(self, s: str, t: str) -> bool:
		
		sDict = {}
		tDict = {}
	
		for i in range(len(s)):
	
			if sDict.__contains__(s[i]) and tDict.__contains__(t[i]):
				if sDict[s[i]] != t[i] or tDict[t[i]] != s[i]:
					return False
			elif sDict.__contains__(s[i]) or tDict.__contains__(t[i]):
				return False
			else:
				sDict[s[i]] = t[i]
				tDict[t[i]] = s[i]
	
		return True
