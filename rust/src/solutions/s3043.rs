use std::collections::HashMap;

struct Solution;

struct Node {
    children: HashMap<char, Node>,
    terminal: bool
}

impl Node {
    pub fn new() -> Self {
        Node {
            children: HashMap::new(),
            terminal: false
        }
    }
}

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut longest_prefix_length = 0;
        let mut trie: Node = Node::new();

        for num in arr1 {
            let mut curr = &mut trie;
            let word = num.to_string();

            for c in word.chars() {
                if !curr.children.contains_key(&c) {
                    curr.children.insert(c, Node::new());
                }
                curr = curr.children.get_mut(&c).unwrap();
            }

            curr.terminal = true;
        }

        for num in arr2 {
            let mut curr = &mut trie;
            let mut prefix_streak = 0;
            let word = num.to_string();

            for c in word.chars() {
                if let Some(v) = curr.children.get_mut(&c) {
                    prefix_streak += 1;
                    curr = v;
                }
                else {
                    break
                }
            }
            longest_prefix_length = longest_prefix_length.max(prefix_streak);
        }
        longest_prefix_length
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_3043() {
        let arr1 = vec![1,10,100];
        let arr2 = vec![1000];

        assert_eq!(Solution::longest_common_prefix(arr1, arr2), 3)
    }
}