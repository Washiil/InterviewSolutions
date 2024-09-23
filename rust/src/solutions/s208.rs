use std::collections::HashMap;

struct TrieNode {
    pub children: HashMap<char, TrieNode>,
    pub terinary: bool
}

impl TrieNode {
    pub fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            terinary: false,
        }
    }
}

struct Trie {
    pub root: TrieNode
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {

    fn new() -> Self {
        Trie {
            root: TrieNode::new(),
        }
    }
    
    fn insert(&mut self, word: String) {
        let mut curr = &mut self.root;

        for c in word.chars() {
            if !curr.children.contains_key(&c) {
                curr.children.insert(c, TrieNode::new());
            }

            curr = curr.children.get_mut(&c).unwrap();
        }

        curr.terinary = true;
    }
    
    fn search(&self, word: String) -> bool {
        let mut curr = &self.root;

        for c in word.chars() {
            if let Some(child) = curr.children.get(&c) {
                curr = child;
            }
            else {
                return false;
            }
        }

        curr.terinary
    }
    
    fn starts_with(&self, prefix: String) -> bool {
        let mut curr = &self.root;

        for c in prefix.chars() {
            if let Some(child) = curr.children.get(&c) {
                curr = child;
            }
            else {
                return false;
            }
        }

        true
    }
}