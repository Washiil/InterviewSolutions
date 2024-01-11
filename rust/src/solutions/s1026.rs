use crate::solutions::utils::TreeNode;
use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

struct Solution;

impl Solution {
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        use std::collections::HashSet;

        let mut output = HashSet::new();

        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, a: &mut Vec<i32>, output: &mut HashSet<i32>) {
            if let Some(n) = node {
                let n_ref = n.borrow();
                a.push(n_ref.val);
                dfs(n_ref.left.clone(), &mut a.clone(), output);
                dfs(n_ref.right.clone(), &mut a.clone(), output);
                output.insert((a.iter().max().unwrap() - a.iter().min().unwrap()).abs());
            }
        }

        dfs(root, &mut Vec::new(), &mut output);
        *output.iter().max().unwrap_or(&0)
    }
}

mod tests {
    use super::*;

    #[test]
    fn test1() {}
}
