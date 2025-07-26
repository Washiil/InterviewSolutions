class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        seen = set()
        root = head
        
        while root.next:
            if root in seen:
                return True
            seen.add(root)
            root = root.next
        
        return False
