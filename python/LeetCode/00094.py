from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
