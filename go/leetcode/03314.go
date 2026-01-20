package main

func minBitwiseArray(nums []int) []int {
	n := len(nums)
	ans := make([]int, n, n)

	for i := range n {
		ans[i] = -1

		for j := range nums[i] {
			if j|(j+1) == nums[i] {
				ans[i] = j
				break
			}
		}
	}

	return ans
}
