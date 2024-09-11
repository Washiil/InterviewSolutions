struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        // Keep a bit value and just xor is ove and over and whatever is leftove ris the number

        let mut bits = 0;

        for i in &nums {
            bits ^= i
        };

        bits
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_136() {
        let nums = vec![0, 2, 3, 2, 3, 9, 0, 7, 7];
        assert_eq!(Solution::single_number(nums), 9);
    }
}