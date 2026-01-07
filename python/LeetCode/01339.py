from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(self, root: Optional[TreeNode]) -> int:
    # Maximize two subtrees
    subsums = []

    def subtree_sum(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = subtree_sum(node.left)
        right = subtree_sum(node.right)

        total = left + node.val + right
        subsums.append(total)
        return total

    treesum = subtree_sum(root)
    best = 0
    for subtree in subsums:
        best = max(best, subtree * (treesum - subtree))
    return int(best % (1e9 + 7))
