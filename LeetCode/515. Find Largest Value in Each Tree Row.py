from typing import Optional


class TreeNode:
    def __init__(self) -> None:
        left: TreeNode
        val: int
        right: TreeNode


def largestValues(self, root: Optional[TreeNode]) -> list[int]:
    depths = []

    def recur(node: Optional[TreeNode], depth: int) -> int:
        if len(depths) <= depth:
            depths.append([])
        if not node:
            return

        depths[depth].append(node.val)
        if node.left:
            recur(node.left, depth + 1)
        if node.right:
            recur(node.right, depth + 1)

    recur(root, 0)
    print(depths)
    return [max(i) for i in depths if len(i) > 0]
