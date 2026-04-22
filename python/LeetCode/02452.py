from typing import List

def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
    query_length = len(queries)
    dict_legnth = len(dictionary)
    word_length = len(queries[0])
    output = []

    for i in range(query_length):
        for j in range(dict_legnth):
            edits = 0
            for k in range(word_length):
                if queries[i][k] != dictionary[j][k]:
                    edits += 1

            if edits <= 2:
                output.append(queries[i])
                break

    return output