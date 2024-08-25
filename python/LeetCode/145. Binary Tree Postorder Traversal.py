class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    output = []
    output += self.postorderTraversal(root.left)
    output += self.postorderTraversal(root.right)
    output += [root.val]
    
    return output