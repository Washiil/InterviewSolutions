struct Solution;

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut duplicate: i32 = -1;
        let mut missing: i32 = -1;
        for i in 1..nums.len() + 1 {
            let count = nums.iter().filter(|&n| *n == i as i32).count();
            if count == 2 {
                duplicate = i as i32;
            }
            else if count == 0 {
                missing = i as i32;
            };
        }
        return vec![duplicate, missing];
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = vec![1,2,2,4];
        assert_eq!(Solution::find_error_nums(input), vec![2,3]);
    }

    #[test]
    fn test2() {
        let input = vec![1,1];
        assert_eq!(Solution::find_error_nums(input), vec![1,2]);
    }
}
