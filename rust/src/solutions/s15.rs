use std::cmp::Ordering;

struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let length = nums.len();

        let mut nums = nums.clone();
        nums.sort();

        let mut res: Vec<Vec<i32>> = vec![];

        for i in 0..length {
            if i > 0 && nums[i] == nums[i - 1] {
                continue
            }

            let mut left = i + 1;
            let mut right = length - 1;

            while left < right {
                let total = nums[i] + nums[left] + nums[right];

                match total.cmp(&0) {
                    Ordering::Less => {
                        left += 1;
                    },
                    Ordering::Equal => {
                        res.push(vec![nums[i], nums[left], nums[right]]);
                        left += 1;

                        while nums[left] == nums[left - 1] && left < right {
                            left += 1;
                        }
                    },
                    Ordering::Greater => {
                        right -= 1;
                    },
                }
            }
        }

        res
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_15() {
        use super::*;

        let input = vec![-1,0,1,2,-1,-4];
        assert_eq!(Solution::three_sum(input), vec![vec![-1, -1, 2], vec![-1, 0, 1]])
    }
}
