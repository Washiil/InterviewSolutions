from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], bit_str: str) -> int:
        if not node:
            return 0

        bit_str += str(node.val)
        if not node.left and not node.right:
            return int(bit_str, 2)

        return dfs(node.left, bit_str) + dfs(node.right, bit_str)

    return dfs(root, '')