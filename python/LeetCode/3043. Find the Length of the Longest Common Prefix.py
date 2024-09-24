from typing import List

def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    longest_prefix = 0
    trie = {}

    for num in arr1:
        word = str(num)
        curr = trie

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
    
    for num in arr2:
        word = str(num)
        curr = trie
        prefix_streak = 0
        
        for c in word:
            if c in curr:
                prefix_streak += 1
                curr = curr[c]
            else:
                break

        longest_prefix = max(prefix_streak, longest_prefix)
    
    return longest_prefix
