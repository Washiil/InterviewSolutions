use std::cmp::{min, max};

struct Solution;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut max_area: i32 = 0;
        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;

        while left < right {
            let volume = (right - left) as i32 * min(height[left], height[right]);
            max_area = max(max_area, volume);

            if height[left] < height[right] {
                left += 1;
            }
            else {
                right -= 1;
            }
        }

        max_area
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_11() {
        let input = vec![1,8,6,2,5,4,8,3,7];

        assert_eq!(Solution::max_area(input), 49)
    }
}