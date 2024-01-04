# Explanation https://www.youtube.com/watch?v=s9fokUqJ76A

def balanced_parens(n):
    result = []
    stack = []
    
    def recurse(open, closed):
        if open == closed == n:
            result.append(''.join(stack))
            return
        
        if open < n:
            stack.append("(")
            recurse(open + 1, closed)
            stack.pop()
            
        if closed < open:
            stack.append(")")
            recurse(open, closed + 1)
            stack.pop()
        
    
    recurse(0, 0)
    return result