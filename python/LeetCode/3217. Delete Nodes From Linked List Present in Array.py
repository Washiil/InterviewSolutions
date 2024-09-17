from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)
    while head.next:
        if head.val not in nums:
            break
        head = head.next

    output = head

    back = head
    forward = head

    while forward.next != None:
        forward = forward.next
        if forward.val not in nums:
            back.next = forward
            back = forward

    if forward.val in nums:
        back.next = None

    return head
    

