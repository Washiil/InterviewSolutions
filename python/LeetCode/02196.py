class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
    nodes: dict[int, TreeNode] = {}
    rootCandidates = set()
    hasIncomingEdge = set()
    for parent, child, isLeft in descriptions:
        hasIncomingEdge.add(child)

        if parent not in nodes:
            rootCandidates.add(parent)
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        if isLeft:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

    root = (rootCandidates - hasIncomingEdge).pop()
    return nodes[root]
