use crate::solutions::utils::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;

impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        if let Some(node) = root {
            let node_ref = node.borrow();
            let node_val = node_ref.val;

            let mut output = 0;
            if node_val >= low && node_val <= high {
                output += node_val;
            }

            if node_val > low {
                output += Solution::range_sum_bst(node_ref.left.clone(), low, high);
            }

            if node_val < high {
                output += Solution::range_sum_bst(node_ref.right.clone(), low, high);
            }

            return output;
        } else {
            return 0;
        }
    }
}

mod tests {
    use crate::solutions::s938::Solution;
    use crate::solutions::utils::TreeNode;
    use std::cell::RefCell;
    use std::rc::Rc;

    #[test]
    fn test1() {
        let root = Rc::new(RefCell::new(TreeNode::new(10)));
        let left_child = Rc::new(RefCell::new(TreeNode::new(5)));
        let right_child = Rc::new(RefCell::new(TreeNode::new(15)));

        root.borrow_mut().left = Some(left_child.clone());
        root.borrow_mut().right = Some(right_child.clone());

        let left_grandchild = Rc::new(RefCell::new(TreeNode::new(3)));
        let left_right_grandchild = Rc::new(RefCell::new(TreeNode::new(7)));
        let right_grandchild = Rc::new(RefCell::new(TreeNode::new(18)));

        left_child.borrow_mut().left = Some(left_grandchild.clone());
        left_child.borrow_mut().right = Some(left_right_grandchild.clone());

        right_child.borrow_mut().right = Some(right_grandchild.clone());

        assert_eq!(Solution::range_sum_bst(Some(root), 7, 15), 32)
    }
}
