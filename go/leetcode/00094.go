package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func helper(root *TreeNode, res *[]int) {
	if root == nil {
		return
	}
	helper(root.Left, res)
	*res = append(*res, root.Val)
	helper(root.Right, res)
}

func inorderTraversal(root *TreeNode) []int {
	result := make([]int, 0)
	helper(root, &result)
	return result
}
