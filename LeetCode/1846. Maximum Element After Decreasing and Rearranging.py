def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
		x = sorted(arr)
		x[0] = 1

		for i in range(1, len(x)):
				diff = abs(x[i] - x[i - 1])
				if diff > 1:
						x[i] -= (diff - 1)
		
		return max(x)