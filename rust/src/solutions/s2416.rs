use std::collections::HashMap;

struct Solution;

struct Node {
    children: HashMap<char, Node>,
    count: i32
}

impl Node {
    pub fn new() -> Self {
        Node {
            children: HashMap::new(),
            count: 0
        }
    }
}

impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        let mut root = Node::new();
        let mut output: Vec<i32> = Vec::new();

        for word in &words {
            let mut curr = &mut root;
            for c in word.chars() {
                if !curr.children.contains_key(&c) {
                    curr.children.insert(c, Node::new());
                }
                curr = curr.children.get_mut(&c).unwrap();
                curr.count += 1;
            }
        }

        for word in &words {
            let mut curr = &mut root;
            let mut total = 0;
            for c in word.chars() {
                curr = curr.children.get_mut(&c).unwrap();
                total += curr.count;
            }
            output.push(total);
        }

        output
    }
}