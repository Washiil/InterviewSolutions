package main

func kLengthApart(nums []int, k int) bool {
	n := len(nums)
	ones := make([]int, 0)

	for i := range n {
		if nums[i] == 1 {
			ones = append(ones, i)
		}
	}

	j := len(ones)
	if j <= 1 {
		return true
	}

	for i := range j - 1 {
		if ones[i+1]-ones[i] < k+1 {
			return false
		}
	}

	return true
}
