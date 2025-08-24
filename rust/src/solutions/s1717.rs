struct Solution;

impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        let mut score = 0;
        // Remove "ab" gives x
        // remove "ba" gives y

        let mut str = s;
        while str.contains("ab") || str.contains("ba") {
            if x > y {
                while let Some(index) = str.find("ab") {
                    str.replace_range(index..index+2, "");
                    score += x
                }

                while let Some(index) = str.find("ba") {
                    str.replace_range(index..index+2, "");
                    score += y
                }
            }
            else {
                while let Some(index) = str.find("ba") {
                    str.replace_range(index..index+2, "");
                    score += y
                }

                while let Some(index) = str.find("ab") {
                    str.replace_range(index..index+2, "");
                    score += x
                }
            }
        }
        score
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = String::from("cdbcbbaaabab");
        assert_eq!(Solution::maximum_gain(input, 4, 5), 20);
    }

    #[test]
    fn test2() {
        let input = String::from("aabbaaxybbaabb");
        assert_eq!(Solution::maximum_gain(input, 5, 4), 20);
    }
}
