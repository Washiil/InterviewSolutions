import re

def solve(s):
    res = re.split('a|e|i|o|u', s)
    highest = 0
    
    for group in res:
        values = list(map((lambda x: ord(x) - 96), group))
        
        if sum(values) > highest:
            highest = sum(values)
    
    return highest