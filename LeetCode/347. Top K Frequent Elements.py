def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    freq = {}

    for i in nums:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1

    l = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[0:k])
    return list(l.keys())
