from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(v1, v2):
    upper = max(v1, v2)
    for i in range(upper, 0, -1):
        if v1 % i == 0 and v2 % i == 0:
            return i
    return -1

def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current.next != None:
        next_node = current.next
        common_divisor = gcd(current.val, next_node.val)
        print(current.val, next_node.val, common_divisor)

        divisor_node = ListNode(common_divisor, next_node)

        current.next = divisor_node
        current = next_node

    return head