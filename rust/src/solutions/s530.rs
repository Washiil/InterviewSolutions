use crate::solutions::utils::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

use std::cmp;

struct Solution;

impl Solution {
    fn inorder(root: Option<Rc<RefCell<TreeNode>>>, node_values: &mut Vec<i32>) {
        if let Some(node) = root {
            Solution::inorder(node.borrow().left.clone(), node_values);
            node_values.push(node.borrow().val);
            Solution::inorder(node.borrow().right.clone(), node_values);
        }
    }

    pub fn min_diff_in_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut node_values = Vec::new();
        Solution::inorder(root, &mut node_values);
        let mut diff = i32::MAX;
        for i in 1..node_values.len() {
            diff = cmp::min(diff, node_values[i] - node_values[i - 1]);
        }
        diff
    }
}

mod tests {
    // Working on a better test constructor
}
