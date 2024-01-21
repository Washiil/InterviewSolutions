use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut count1 = 0;
        let mut count2 = 0;

        for num in nums {
            let temp = count1;
            count1 = count1.max(count2 + num);
            count2 = temp;
        }
        return count1;
    }
}
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = vec![1, 2, 3, 1];
        assert_eq!(Solution::rob(input), 4)
    }

    #[test]
    fn test2() {
        let input = vec![2, 7, 9, 3, 1];
        assert_eq!(Solution::rob(input), 12)
    }
}
