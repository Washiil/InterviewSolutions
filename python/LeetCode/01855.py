def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)

    res = 0

    for i in range(n):
        target = nums1[i]

        left = i
        right = m - 1
        while left < right:
            mid = (left + right + 1) // 2

            if nums2[mid] >= target:
                left = mid
            else:
                right = mid - 1

        res = max(res, left - i)

    return res
