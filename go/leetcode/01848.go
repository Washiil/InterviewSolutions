package main

func getMinDistance(nums []int, target int, start int) int {
    n := len(nums)
    mid := start

    for i := 0; i < n; i++ {
        if mid - i >= 0 {
            if nums[mid - i] == target {
                return i
            }
        }

        if mid + i < n {
            if nums[mid + i] == target {
                return i
            }
        }
    }

    return -1
}
