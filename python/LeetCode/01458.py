from typing import List

def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    # Helper function to solve for the remainder of the arrays starting at i, j
    def dfs(i, j):
        # When we "skip" we need to ensure that our values are the same
        if i == len(nums1) or j == len(nums2):
            return float('-inf')

        # Multiply the current pair (nums1[i] * nums2[j])
        take_curr = (nums1[i] * nums2[j]) + max(0, dfs(i + 1, j + 1))

        # Get the various "skip" options
        skip_i = dfs(i + 1, j)
        skip_j = dfs(i, j + 1)

        # Return the best of the three options
        return max(take_curr, skip_i, skip_j)

    return dfs(0, 0)