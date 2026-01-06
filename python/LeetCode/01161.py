from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    levels = []

    def bfs(node: Optional[TreeNode], level: int):
        if not node:
            return

        if len(levels) < level:
            levels.append(0)

        levels[level - 1] += node.val
        bfs(node.left, level + 1)
        bfs(node.right, level + 1)

    bfs(root, 1)
    return levels.index(max(levels)) + 1
