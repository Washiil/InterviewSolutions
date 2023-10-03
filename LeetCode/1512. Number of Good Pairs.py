def numIdenticalPairs(self, nums: list[int]) -> int:
		pairs = 0
		length = len(nums)
		for i in range(length):
				for j in range(length):
						if i < j and nums[i] == nums[j]:
								pairs += 1
		
		return pairs