package main

func minimumPairRemoval(nums []int) int {
	ops := 0

	for len(nums) > 1 {
		isAscending := true
		minSum := 1<<31 - 1
		targetIndex := -1

		for i := range len(nums) - 1 {
			pairSum := nums[i] + nums[i+1]
			if nums[i] > nums[i+1] {
				isAscending = false
			}

			if pairSum < minSum {
				minSum = pairSum
				targetIndex = i
			}
		}

		if isAscending {
			break
		}

		ops++
		nums[targetIndex] = minSum
		nums = append(nums[:targetIndex+1], nums[targetIndex+2:]...)
	}

	return ops
}
