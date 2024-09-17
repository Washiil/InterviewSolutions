use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut words = HashMap::new();

        for x in s1.split(' ') {
            if let Some(val) = words.get_mut(x) {
                *val += 1
            }
            else {
                words.insert(x, 1);
            }
        }

        for x in s2.split(' ') {
            if let Some(val) = words.get_mut(x) {
                *val = 0;
            }
            else {
                words.insert(x, 1);
            }
        }

        words
            .iter()
            .filter(|&(k, &v)| v == 1)
            .map(|(&k, _)| k.to_string())
            .collect::<Vec<String>>()
    }
}

mod tests {
    use super::*;

    #[test]
    fn test_884() {
        let string_1 = "this apple is sweet".to_string();
        let string_2 = "this apple is sour".to_string();

        assert_eq!(Solution::uncommon_from_sentences(string_1, string_2), vec!["sweet".to_string(),"sour".to_string()]);
    }
}
