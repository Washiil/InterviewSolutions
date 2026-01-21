package main

func minBitwiseArrayV2(nums []int) []int {
	n := len(nums)
	ans := make([]int, n, n)

	for i, x := range nums {
		res := -1
		d := 1
		for (x & d) != 0 {
			res = x - d
			d <<= 1
		}
		ans[i] = res
	}

	return ans
}
