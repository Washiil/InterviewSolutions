struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut output = 0;
        for s in stones.chars() {
            if jewels.contains(s) {
                output += 1;
            }
        }
        return output;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let jewels = "aA".to_string();
        let stones = "aAAbbbb".to_string();
        assert_eq!(Solution::num_jewels_in_stones(jewels, stones), 3);
    }

    #[test]
    fn test2() {
        let jewels = "z".to_string();
        let stones = "ZZ".to_string();
        assert_eq!(Solution::num_jewels_in_stones(jewels, stones), 0);
    }
}
