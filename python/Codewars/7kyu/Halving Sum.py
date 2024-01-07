def halving_sum(n): 
    # your code here
    output = 0
    last = 1
    
    curr = 1
    while last > 0:
        last = n // curr
        print(last)
        output += last
        curr = curr * 2
    
    return output