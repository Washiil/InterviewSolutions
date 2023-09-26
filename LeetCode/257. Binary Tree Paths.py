def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
		res = []
		def search(child: Optional[TreeNode], path: str):
				if child.left != None:
						search(child.left, f'{path}->{child.left.val}')

				if child.right != None:
						search(child.right, f'{path}->{child.right.val}')

				if child.left == None and child.right == None:
						res.append(path)
		search(root, f'{root.val}')

		return res