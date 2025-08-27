from typing import Optional

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.next = left

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow