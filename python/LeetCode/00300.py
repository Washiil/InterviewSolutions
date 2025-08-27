def lengthOfLIS(self, nums: list[int]) -> int:
    # Credit: https://leetcode.com/problems/longest-increasing-subsequence/solutions/4509129/99-54-easy-solution-with-explanation/
    # Dynamic programming is still a struggle
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)