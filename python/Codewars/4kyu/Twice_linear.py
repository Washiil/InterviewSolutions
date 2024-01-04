# Credit for the understanding goes here
# https://medium.com/@peteryun/algo-twice-linear-ba882c587a3e

def dbl_linear(n):
    sequence = [1] 
    x = 0
    y = 0
    
    while(len(sequence) <= n): 
        a = 2 * sequence[x] + 1 
        b = 3 * sequence[y] + 1 
        
        if a > b: 
            sequence.append(b)
            y += 1 
        elif a < b: 
            sequence.append(a)
            x += 1 
        else: 
            sequence.append(a)
            x += 1 
            y += 1
            
    return sequence[n]