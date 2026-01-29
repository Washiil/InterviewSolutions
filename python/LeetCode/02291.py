from typing import List

def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
    n = len(present)

    cache = {}
    def maxProfit(index: int, remainingBudget: int):
        if index == n:
            return 0

        key = (index, remainingBudget)
        if key in cache:
            return cache[key]

        cost = present[index]
        maxBuyingProfit = 0
        maxPassingProfit = maxProfit(index + 1, remainingBudget) + 0
        if remainingBudget >= cost:
            maxBuyingProfit = maxProfit(index + 1, remainingBudget - cost) + (future[index] - cost)

        cache[key] = max(maxPassingProfit, maxBuyingProfit)
        return cache[key]

    return maxProfit(0, budget)
