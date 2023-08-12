def productFib(prod):
    a = 0
    b = 1
    
    while a * b != prod:
        if a * b > prod:
            return [a, b, False]
        a, b = b, a + b
    
    return [a, b, True]