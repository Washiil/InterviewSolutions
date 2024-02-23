class Solution:
    def __init__(self):
        self.node_values = []

    # This in order traversal works due to the structure of binary trees
    # node.left < node.val < node.right
    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)

        self.node_values.append(root.val)

        if root.right is not None:
            self.inorder(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        diff = abs(self.node_values[0] - self.node_values[1])
        for i in range(1, len(self.node_values)):
            diff = min(diff, abs(self.node_values[i - 1] - self.node_values[i]))
        return diff  # reduce(lambda x, y: min(abs(x-y), y), self.node_values)