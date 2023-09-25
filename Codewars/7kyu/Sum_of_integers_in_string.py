def sum_of_integers_in_string(s):
    total = 0
    number = "0"
    for c in s:
        if c.isnumeric():
            number += c
        else:
            total += int(number)
            number = "0"
    return total + int(number)