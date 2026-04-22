package main

import (
	"sort"
)

func solveQueries(nums []int, queries []int) []int {
	n := len(nums)
	
	positions := make(map[int][]int)
	for i, val := range nums {
		positions[val] = append(positions[val], i)
	}

	answer := make([]int, len(queries))

	for i, q := range queries {
		val := nums[q]
		indices := positions[val]
		m := len(indices)

		if m == 1 {
			answer[i] = -1
			continue
		}

		k := sort.SearchInts(indices, q)

		leftNeighborIdx := indices[(k-1+m)%m]
		rightNeighborIdx := indices[(k+1)%m]

		distLeft := getCircularDistance(q, leftNeighborIdx, n)
		distRight := getCircularDistance(q, rightNeighborIdx, n)

		answer[i] = min(distLeft, distRight)
	}

	return answer
}

func getCircularDistance(a, b, n int) int {
	dist := abs(a - b)
	return min(dist, n-dist)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
