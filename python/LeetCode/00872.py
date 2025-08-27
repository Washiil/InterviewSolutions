from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def recur(node: TreeNode) -> list[int]:
        output = []
        if node.left or node.right:
            if node.left:
                output.extend(recur(node.left))
            if node.right:
                output.extend(recur(node.right))
        else:
            output.append(node.val)
        return output
    
    r1 = recur(root1)
    r2 = recur(root2)
    print(f'{r1}\n{r2}')
    return r1 == r2