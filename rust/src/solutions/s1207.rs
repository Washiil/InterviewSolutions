use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut counts: HashMap<i32, usize> = HashMap::new();
        for x in arr {
            let entry = counts.entry(x).or_insert(0);
            *entry += 1;
        }
        let values: Vec<usize> = counts.values().cloned().collect();
        let unique_values = values.clone().into_iter().collect::<HashSet<_>>();

        return values.len() == unique_values.len();
    }
}

mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = vec![1,2,2,1,1,3];
        assert_eq!(Solution::unique_occurrences(input), true)
    }

    #[test]
    fn test2() {
        let input = vec![1, 2];
        assert_eq!(Solution::unique_occurrences(input), false)
    }

    #[test]
    fn test3() {
        let input = vec![-3,0,1,-3,1,1,1,-3,10,0];
        assert_eq!(Solution::unique_occurrences(input), true)
    }
}
