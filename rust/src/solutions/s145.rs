use std::collections::HashMap;
use std::rc::Rc;
use std::cell::RefCell;

use super::utils::TreeNode;

struct Solution;

impl Solution {
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut output: Vec<i32> = Vec::new();
        
        if let Some(node) = root {
            let node = node.borrow();

            output.append(&mut Self::postorder_traversal(node.left.clone()));
            output.append(&mut Self::postorder_traversal(node.right.clone()));

            output.push(node.val);
        }
        
        output
    }
}

mod tests {
    use super::*;

    // Havent implemented great tests cases for trees yet
}
