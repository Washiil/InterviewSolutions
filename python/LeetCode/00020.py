def isValid(self, s: str) -> bool:
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    opening = brackets.values()
    closing = brackets.keys()

    stack = []

    for x in s:
        if x in opening:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if bracket != brackets[x]:
                return False
    
    if len(stack) != 0:
        return False
    return True
