def majorityElement(self, nums: List[int]) -> List[int]:
		m = len(nums) // 3
		values = {}
		for i in nums:
				values[i] = values.get(i, 0) + 1

		return [x for x in values if values[x] > m]