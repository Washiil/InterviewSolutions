use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let t1_len = text1.len();
        let t2_len = text2.len();

        let mut dp_matrix = vec![vec![0; t2_len + 1]; t1_len + 1];

        let text1: Vec<char> = text1.chars().collect();
        let text2: Vec<char> = text2.chars().collect();

        for i in 1..t1_len + 1 {
            for j in 1..t2_len + 1 {
                if text1[i - 1] == text2[j - 1] {
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1;
                } else {
                    dp_matrix[i][j] = dp_matrix[i - 1][j].max(dp_matrix[i][j - 1]);
                }
            }
        }
        return dp_matrix[t1_len][t2_len];
    }
}

mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = ("abcde".to_string(), "ace".to_string());
        assert_eq!(Solution::longest_common_subsequence(input.0, input.1), 3)
    }
}
