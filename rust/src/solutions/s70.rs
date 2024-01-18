use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn climb(n: i32, memo: &mut HashMap<i32, i32>) -> i32 {
        if n == 0 || n == 1 {
            return 1;
        }
        if !memo.contains_key(&n) {
            let v1 = Solution::climb(n - 1, memo);
            let v2 = Solution::climb(n - 2, memo);
            memo.insert(n, v1 + v2);
        }

        return memo.get(&n).unwrap().clone();
    }

    pub fn climb_stairs(n: i32) -> i32 {
        let mut memo: HashMap<i32, i32> = HashMap::new();
        return Solution::climb(n, &mut memo);
    }
}
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = 2;
        assert_eq!(Solution::climb_stairs(input), 2)
    }

    #[test]
    fn test2() {
        let input = 3;
        assert_eq!(Solution::climb_stairs(input), 3)
    }
}
