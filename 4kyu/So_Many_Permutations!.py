def permutations(s):
    result = set([s])                                    # init set using list
    if len(s) == 2:                                      # base case
        result.add(s[1] + s[0])

    elif len(s) > 2:
        for i, c in enumerate(s):                        # loop through current string
            for perm in permutations(s[:i] + s[i + 1:]): # recurse with the string slice
                result.add(c + perm)
    
    return list(result)