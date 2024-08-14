use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut seen: HashSet<i32> = HashSet::new();

        let mut n: i32 = n;
        while seen.insert(n) {
            n = n.to_string()
                .chars()
                .map(|c| {
                    let digit = c.to_digit(10).unwrap();
                    return (digit * digit) as i32;
                })
                .sum();
            if n == 1 {
                return true;
            }
        }

        return false;
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_202() {
        let result = Solution::is_happy(19);
        assert_eq!(result, true);

        let result = Solution::is_happy(2);
        assert_eq!(result, false);
    }
}
