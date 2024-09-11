use super::utils::ListNode;

struct Solution {}

impl Solution {
    fn gcd(v1: i32, v2: i32) -> i32 {
        let upper = v1.max(v2);
        for i in (0..=upper).rev() {
            if v1 % i == 0 && v2 % i == 0 {
                return i;
            }
        }
        -1
    }

    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = head;
        let mut current = &mut head;

        while let Some(node) = current {
            if node.next.is_none() {
                break;
            }
            let next = node.next.take().unwrap();
            node.next = Some(Box::new(ListNode {
                val: Self::gcd(node.val, next.val),
                next: Some(next),
            }));
            current = &mut node.next.as_mut().unwrap().next;
        }

        head
    }
}