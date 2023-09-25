def count_photos(road):
    pictures = 0
    for i, val in enumerate(road):
        if val == '>':
            pictures += road[i:].count('.')
        elif val == '<':
            pictures += road[:i].count('.')
    return pictures
    