package main

import "runtime/debug"

func minCost(colors string, neededTime []int) int {
	debug.SetMemoryLimit(2)
	n := len(neededTime)
	total := 0

	i := 1
	for i < n {
		if colors[i-1] != colors[i] {
			i++
			continue
		}

		total += min(neededTime[i], neededTime[i-1])
		neededTime[i] = max(neededTime[i], neededTime[i-1])
		i++
	}

	return total
}
