use crate::solutions::utils::TreeNode;
use std::cell::RefCell;
use std::collections::{HashMap, HashSet};
use std::rc::Rc;

struct Solution;

impl Solution {
    pub fn convert(
        root: Option<Rc<RefCell<TreeNode>>>,
        parent: i32,
        tree_map: &mut HashMap<i32, HashSet<i32>>,
    ) {
        match root {
            Some(node) => {
                let node_ref = node.borrow();
                let node_val = node_ref.val;

                if !tree_map.contains(&node_val) {
                    tree_map.insert(node_val, HashSet::new());
                }

                let mut adjacent_list = tree_map.get(&node_val).unwrap();

                if parent != 0 {
                    adjacent_list.insert(parent);
                }

                if node_ref.left.is_some() {
                    adjacent_list.insert(node_ref.left.unwrap().borrow().val);
                }
            }
            None => {}
        }
    }
}
