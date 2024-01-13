pub struct Solution;

impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut count: [i32; 26] = [0; 26];

        for c in s.chars() {
            count[((c as u8) - 97) as usize] += 1;
        }
        for c in t.chars() {
            count[((c as u8) - 97) as usize] -= 1;
        }

        let x = count.iter_mut().map(|x| x.abs()).collect::<Vec<i32>>();
        return x.iter().sum::<i32>() / 2;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let s = "bab".to_string();
        let t = "aba".to_string();

        assert_eq!(Solution::min_steps(s, t), 1);
    }

    #[test]
    fn test2() {
        let s = "leetcode".to_string();
        let t = "practice".to_string();

        assert_eq!(Solution::min_steps(s, t), 5);
    }

    #[test]
    fn test3() {
        let s = "anagram".to_string();
        let t = "mangaar".to_string();

        assert_eq!(Solution::min_steps(s, t), 0);
    }
}
