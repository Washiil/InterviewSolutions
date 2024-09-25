class Node:
    def __init__(self):
        self.children = {}
        self.weight = 0

def sumPrefixScores(self, words: List[str]) -> List[int]:
    # Essentially a weighted Trie
    root = self.Node()
    output = []

    for word in words:
        curr = root

        for c in word:
            if c not in curr.children:
                curr.children[c] = self.Node()
            
            curr = curr.children[c]
            curr.weight += 1
            
    result = []
    for word in words:
        curr = root
        total = 0
        for char in word:
            curr = curr.children[char]
            total += curr.weight
        result.append(total)
    
    return result