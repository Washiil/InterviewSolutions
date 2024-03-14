# Credit for this one goes to https://leetcode.com/CS_MONKES
def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
    pri={0:1}
    res=0
    total=0
    for i in nums:
        total += i
        res += pri.get(total - goal, 0)
        pri[total] = pri.get(total, 0) + 1
    return res