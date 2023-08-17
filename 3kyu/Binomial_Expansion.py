import math


def expand(expr):
    # Lets solve this using pascals triangle
    # (ax+b)^n
    parts = expr.split('^')
    # (ax+b)  |  n
    exponent = int(parts[1])
    if exponent == 0:
        return '1'

    expression = parts[0][1:-1]  # Strip the parentheses
    index = 0
    for char in expression:
        if char.isalpha():
            break
        else:
            index += 1
    

    ax = expression[:index + 1]
    variable = ax[-1]
    print(ax[1:-1])
    asasdada = int(ax[1:-1])
    # a = int(ax[1:-1]) *  -1 if ax[0] == '-' else int(ax[0:-1])
    b = expression[index + 1:]

    print('\nExpression: ' + expr)
    print(f'a: {a}')
    print(f'ax: {ax}')
    print(f'b:  {b}')

    pascal = []
    for i in range(exponent + 1):
        pascal.append(math.comb(exponent, i))

    return ''


print(expand("(x+1)^0"))
print(expand("(x+1)^1"))
print(expand("(x+1)^2"))

print(expand("(x-1)^0"))
print(expand("(x-1)^1"))
print(expand("(x-1)^2"))

print(expand("(5m+3)^4"))
print(expand("(2x-3)^3"))
print(expand("(7x-7)^0"))

print(expand("(-5m+3)^4"))
print(expand("(-2k-3)^3"))
print(expand("(-7x-7)^0"))
