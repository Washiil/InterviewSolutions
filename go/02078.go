package main

func maxDistance(colors []int) int {
    n := len(colors)
    max_dist := 0

    for i := 0; i < n; i++ {
        for j := i + max_dist; j < n; j++ {
            if colors[i] == colors[j] {
                continue
            }
            
            if j - i > max_dist {
                max_dist = j - i
            }
        }
    }

    return max_dist
}
