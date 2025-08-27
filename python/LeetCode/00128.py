def longestConsecutive(self, nums: list[int]) -> int:
    if len(nums) < 1:
        return 0
    x = sorted(nums)
    longest = 0
    curr = 0
    previous = x[0]
    print(x)
    for i in x:
        if i == previous + 1:
            curr += 1
            if curr >= longest:
                longest = curr
        else:
            curr = 0
        previous = i
    return longest + 1
