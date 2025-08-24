def getDecimalValue(self, head: Optional[ListNode]) -> int:
    total = 0
    
    values = []
    root = head
    while root:
        values.append(root.val)
        root = root.next
    
    n = len(values) - 1
    for i in values:
        total += i * (2 ** n)
        n -= 1
    
    return total
