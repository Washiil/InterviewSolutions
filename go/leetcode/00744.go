package main

func nextGreatestLetter(letters []byte, target byte) byte {
	if letters[len(letters)-1] <= target {
		return letters[0]
	}

	n := len(letters)
	high := n - 1
	low := 0

	for low <= high {
		mid := (low + high) / 2
		if letters[mid] <= target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return letters[low]
}
