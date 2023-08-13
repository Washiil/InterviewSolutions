def josephus(items,k):
    soldiers = items
    dead = []
    i = 0
    while len(soldiers) > 0:               # Loop until all soldiers dead
        j = (i + k - 1) % len(soldiers)    # Handle wrapping around the list
        dead.append(soldiers[j])           # Copy soldier to dead list
        del soldiers[j]                    # "Kill" the soldier
        i = j if j < len(soldiers) else 0  # Handle end case with one soldier left
    return dead