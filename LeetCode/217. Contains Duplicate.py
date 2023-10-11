def containsDuplicate(self, nums: list[int]) -> bool:
		return False if len(nums) == len(set(nums)) else True