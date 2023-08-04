class Solution:

	""" 77. Combinations """

	def combine(self, n: int, k: int) -> List[List[int]]:

		side_list = []
		result = []

		if k>1:
			for i in range(n-k+1):

				side_list = [n-i]
				temp = [l for l in self.combine(n-i-1,k-1)]
				result = result + [side_list + t for t in temp]

		else:
			for i in range(1,n+1):
				result.append([i])

		return result

	def combine(self, n: int, k: int) -> List[List[int]]:

		arr = []
		for i in range(1,n+1):
			arr.append(i)

		return list(combinations(arr, k))
