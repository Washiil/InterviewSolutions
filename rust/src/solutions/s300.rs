pub fn length_of_lis(nums: Vec<i32>) -> i32 {
    if nums.is_empty() {
        return 0;
    }

    let length = nums.len();
    let mut dp = vec![1; length];

    for i in 1..length {
        for j in 0..i {
            if nums[i] > nums[j] {
                dp[i] = dp[i].max(dp[j] + 1);
            }
        }
    }

    return dp.into_iter().max().unwrap_or(0);
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        let input = vec![10, 9, 2, 5, 3, 7, 101, 18];
        assert_eq!(super::length_of_lis(input), 4)
    }

    #[test]
    fn test2() {
        let input = vec![0, 1, 0, 3, 2, 3];
        assert_eq!(super::length_of_lis(input), 4)
    }

    #[test]
    fn test3() {
        let input = vec![7, 7, 7, 7, 7, 7, 7];
        assert_eq!(super::length_of_lis(input), 1)
    }
}
