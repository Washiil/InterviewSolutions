package main

func intAbs(val int) int {
	if val < 0 {
		return val * -1
	}
	return val
}

func minTimeToVisitAllPoints(points [][]int) int {
	distance := 0

	for i := 1; i < len(points); i++ {
		x1, y1 := points[i-1][0], points[i-1][1]
		x2, y2 := points[i][0], points[i][1]

		distance += max(intAbs(x2-x1), intAbs(y2-y1))
	}
	return distance
}
