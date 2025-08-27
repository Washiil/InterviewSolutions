def deleteNode(self, node):
    prev = None
    curr = node
    while curr.next != None:
        curr.val = curr.next.val
        prev = curr
        curr = curr.next
    
    prev.next = None