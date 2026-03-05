package main

func minOperations(s string) int {
	c1 := 0
	c2 := 0

	for i, c := range s {
		if i%2 == 0 {
			if c == '1' {
				c1 += 1
			} else {
				c2 += 1
			}
		} else {
			if c == '1' {
				c2 += 1
			} else {
				c1 += 1
			}
		}
	}
	if c1 < c2 {
		return c1
	}
	return c2
}
