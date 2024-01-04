def score(dice):
    values = {}
    total = 0
    for val in dice:
        if val in values.keys():
            values[val] += 1
        else:
            values[val] = 1
    
    for key, value in values.items():
        while value >= 3:
            if key == 1:
                total += 1000
            else:
                total += key * 100
            value = value - 3

        if value < 3:
            if key == 1:
                total += 100 * value
            elif key == 5:
                total += 50 * value
        
    return total