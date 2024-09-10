use std::{borrow::Borrow, collections::{HashMap, HashSet}};

use super::utils::ListNode;


pub struct Solution;

impl Solution {
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let nums = nums.into_iter().collect::<HashSet<i32>>();
        let mut head = head;

        // Handling the case in which the head element is not valid
        while let Some(node) = head.as_ref() {
            if !nums.contains(&node.val) {
                break;
            }
            head = head.unwrap().next;
        }

        head
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    // Still havent implemented linked list test macro
}
