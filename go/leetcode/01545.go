package main

func findKthBit(n int, k int) byte {
	if n == 1 {
		return '0'
	}

	length := (1 << n) - 1
	mid := (length / 2) + 1

	if k == mid {
		return '1'
	} else if k < mid {
		return findKthBit(n-1, k)
	} else if k > mid {
		corresponding_k := length - k + 1
		res := findKthBit(n-1, corresponding_k)
		if res == '0' {
			return '1'
		} else {
			return '0'
		}
	}

	return '0'
}
