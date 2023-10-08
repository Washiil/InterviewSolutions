def solution(number):
    if number <= 0:
        return 0
    
    total = 0
    number -= 1 # stupid fix
    while number > 0:
        if number % 3 == 0 or number % 5 == 0:
            total += number
        number -= 1
    return total