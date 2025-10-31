package main

func sumZero(n int) []int {
	arr := make([]int, 0, 100)
	limit := (n / 2) + 1

	if n%2 != 0 {
		arr = append(arr, 0)
	}

	for i := 1; i < limit; i++ {
		arr = append(arr, i)
		arr = append(arr, i*-1)
	}

	return arr
}
