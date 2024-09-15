struct Solution;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let maximum = nums.iter().max().unwrap();

        let mut output = 0;
        let mut streak = 0;

        for num in &nums {
            if num == maximum {
                streak += 1;
            }
            else if streak > 0 {
                output = output.max(streak);
                streak = 0;
            }
        }
        output = output.max(streak);
        return output;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_2419() {
        let nums = vec![1,2,3,3,2,2];
        assert_eq!(Solution::longest_subarray(nums), 2);

        let nums = vec![1,2,3,4];
        assert_eq!(Solution::longest_subarray(nums), 1);
    }
}
