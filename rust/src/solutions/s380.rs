use rand::seq::SliceRandom;
use std::collections::HashSet;

struct RandomizedSet {
    items: HashSet<i32>,
    values: Vec<i32>,
}

impl RandomizedSet {
    fn new() -> Self {
        RandomizedSet {
            items: HashSet::new(),
            values: Vec::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if !self.items.insert(val) {
            false
        } else {
            self.values.push(val);
            true
        }
    }

    fn remove(&mut self, val: i32) -> bool {
        if !self.items.remove(&val) {
            false
        } else {
            if let Some(pos) = self.values.iter().position(|&x| x == val) {
                self.values.remove(pos);
            }
            true
        }
    }

    fn get_random(&self) -> i32 {
        self.values.choose(&mut rand::thread_rng()).unwrap().clone()
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test1() {
        // Unsure how to test
    }
}
