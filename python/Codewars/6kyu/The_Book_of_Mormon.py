def mormons(starting_number, reach, target):
    missions = 0
    mormons = starting_number
    while mormons < target:
        mormons += mormons * reach
        missions += 1
    return missions