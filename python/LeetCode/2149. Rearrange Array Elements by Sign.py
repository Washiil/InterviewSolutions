def rearrangeArray(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    pos_ptr = 0
    neg_ptr = 1
    for i in nums:
        if i < 0:
            res[neg_ptr] = i
            neg_ptr += 2
        else:
            res[pos_ptr] = i
            pos_ptr += 2
    return res