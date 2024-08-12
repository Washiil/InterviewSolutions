use std::collections::HashSet;

use super::s300::length_of_lis;

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen: HashSet<char> = HashSet::new();
        let mut max = 0;

        let length = s.len();
        let chars = s.chars().collect::<Vec<char>>();

        for i in 0..length {
            let mut j = i;
            while j < length && seen.insert(chars[j]) {
                j += 1;
            }

            max = max.max(seen.len());
            seen.clear();
        }
        

        return max as i32;
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_length_of_longest_substring() {
        let result = Solution::length_of_longest_substring("abcabcbb".to_string());
        assert_eq!(result, 3);

        let result = Solution::length_of_longest_substring("bbbbb".to_string());
        assert_eq!(result, 1);

        let result = Solution::length_of_longest_substring("aab".to_string());
        assert_eq!(result, 2);
    }
}
