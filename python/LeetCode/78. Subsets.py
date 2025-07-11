class Solution:
    def subsets(self, nums: List[int]):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])

        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()
