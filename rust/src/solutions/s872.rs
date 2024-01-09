use std::cell::RefCell;
use std::rc::Rc;
use crate::solutions::utils::TreeNode;

struct Solution;

impl Solution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn recur(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
            let mut output = vec![];
            if let Some(node) = root {
                let node_ref = node.borrow();
                let node_val = node_ref.val;

                if node_ref.left.is_some() || node_ref.right.is_some() {
                    if node_ref.left.is_some() {
                        output.append(&mut recur(node_ref.left.clone()))
                    }
                    if node_ref.right.is_some() {
                        output.append(&mut recur(node_ref.right.clone()))
                    }
                }
                else {
                    output.push(node_val);
                }
            }
            output
        }
        return recur(root1) == recur(root2);
    }
}

mod tests {
    use super::*;
    use crate::solutions::utils::TreeNode;
    use std::cell::RefCell;
    use std::rc::Rc;

    #[test]
    fn test1() {
        // Working on a better test constructor
    }
}