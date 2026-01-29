package main

func maximumProfit(present []int, future []int, budget int) int {
	n := len(present)

	cache := make([][]int, n)
	inCache := make([][]bool, n)
	for i := range cache {
		cache[i] = make([]int, budget+1)
		inCache[i] = make([]bool, budget+1)

		for j := range cache[i] {
			cache[i][j] = 0
			inCache[i][j] = false
		}
	}

	var maxProfit func(index int, balance int) int
	maxProfit = func(index int, balance int) int {
		if index == n {
			return 0
		}

		if inCache[index][balance] {
			return cache[index][balance]
		}

		cost := present[index]
		profit := future[index] - present[index]

		passingMaxProfit := maxProfit(index+1, balance)
		buyingMaxProfit := 0
		if balance >= cost && profit > 0 {
			buyingMaxProfit = maxProfit(index+1, balance-cost) + profit
		}

		cache[index][balance] = max(passingMaxProfit, buyingMaxProfit)
		inCache[index][balance] = true
		return cache[index][balance]
	}

	return maxProfit(0, budget)
}
