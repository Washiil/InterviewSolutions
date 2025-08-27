from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0

    output = root.val if root.val >= low and root.val <= high else 0

    if root.left:
        output += self.rangeSumBST(root.left, low, high)
    if root.right:
        output += self.rangeSumBST(root.right, low, high)
    
    return output