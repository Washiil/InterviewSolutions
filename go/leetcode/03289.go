package main

func getSneakyNumbers(nums []int) []int {
	seen := make(map[int]struct{})

	output := make([]int, 0, 2)

	for _, num := range nums {
		if _, ok := seen[num]; ok {
			output = append(output, num)
			if len(output) == 2 {
				return output
			}
		}
		seen[num] = struct{}{}
	}

	return output
}
