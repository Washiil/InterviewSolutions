package main

func longestSubarray(nums []int) int {
	inds := make([]int, 0, len(nums)/2)
	inds = append(inds, -1)
	for i, n := range nums {
		if n == 0 {
			inds = append(inds, i)
		}
	}
	inds = append(inds, len(nums))

	maxLen := 0

	if len(inds) == 2 {
		return len(nums) - 1
	}

	for i := 1; i < len(inds)-1; i++ {
		maxLen = max(maxLen, inds[i+1]-inds[i-1]-2)
	}

	return maxLen
}
