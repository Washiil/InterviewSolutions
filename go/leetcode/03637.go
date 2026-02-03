package main

func isTrionic(nums []int) bool {
	n := len(nums)
	i := 1

	for i < n && nums[i-1] < nums[i] {
		i += 1
	}
	p := i - 1

	for i < n && nums[i-1] > nums[i] {
		i += 1
	}
	q := i - 1

	for i < n && nums[i-1] < nums[i] {
		i += 1
	}
	flag := i - 1

	return (p != 0) && (q != p) && (flag == n-1 && flag != q)
}
