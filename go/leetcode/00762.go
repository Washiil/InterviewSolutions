package main

/*
Bounded by Right <= 10^6
10_000_000 = 0b100110001001011010000000
24 bits meaning 24 is max number of bits
*/

import (
	"math/bits"
)

var primes = [10]int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

func countPrimeSetBits(left int, right int) int {
	count := 0
	for i := left; i <= right; i++ {
		b := bits.OnesCount(uint(i))
		for _, p := range primes {
			if b == p {
				count++
				break
			}
		}
	}
	return count
}
