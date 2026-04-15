package main

import "slices"

func closestTarget(words []string, target string, startIndex int) int {
	if !slices.Contains(words, target) {
		return -1
	}

	n := len(words)
	for i := range n {
		if words[(startIndex+i)%n] == target {
			return i
		}
		if words[(startIndex-i+n)%n] == target {
			return i
		}
	}

	return -1
}
