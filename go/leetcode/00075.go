package main

func sortColors(nums []int) {
	n := len(nums)

	red := 0
	white := 0
	for _, num := range nums {
		if num == 0 {
			red += 1
		} else if num == 1 {
			white += 1
		}
	}

	for i := 0; i < red; i++ {
		nums[i] = 0
	}

	for i := red; i < red+white; i += 1 {
		nums[i] = 1
	}

	for i := red + white; i < n; i += 1 {
		nums[i] = 2
	}
}
