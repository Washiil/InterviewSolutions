pub struct Solution;

impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'];

        let halfway = s.len() / 2;
        let first = &s[0..halfway];
        let last = &s[halfway..];

        let v1 = first.chars().filter(|x| vowels.contains(x)).count();
        let v2 = last.chars().filter(|x| vowels.contains(x)).count();
        return v1 == v2;
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test1() {
        let input = Solution::halves_are_alike("book".to_string());
        assert_eq!(input, true);
    }

    fn test2() {
        let input = Solution::halves_are_alike("textbook".to_string());
        assert_eq!(input, true);
    }
}
