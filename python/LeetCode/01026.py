from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    output=set()
    def dfs(root, a):
        if root:
            dfs(root.left, a + [root.val])
            dfs(root.right, a + [root.val])
            a.append(root.val)
            output.add(abs(max(a)-min(a)))
    dfs(root, [])
    return max(output)
    