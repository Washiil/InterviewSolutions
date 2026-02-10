package main

func longestBalanced(nums []int) int {
	n := len(nums)
	output := 0

	for i := range n {
		odds := make(map[int]bool, n)
		evens := make(map[int]bool, n)
		for j := i; j < n; j++ {
			if nums[j]%2 == 0 {
				evens[nums[j]] = true
			} else {
				odds[nums[j]] = true
			}

			if len(odds) == len(evens) {
				output = max(output, j-i+1)
			}
		}
	}
	return output
}
