package main

import "math/big"

// Beautiful solution by Anton Mytnik
func hasAllCodes(s string, k int) bool {
	comb, hash, seen := 1<<k, 0, 0

	var bits big.Int
	bits.SetBit(&bits, comb-1, 0)

	for i := 0; i < len(s); i++ {
		hash = ((hash << 1) | int(s[i]-'0')) & (comb - 1)
		if i >= k-1 && bits.Bit(hash) == 0 {
			bits.SetBit(&bits, hash, 1)
			seen++
		}
	}

	return seen == comb
}
