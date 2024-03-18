from typing import List

def count_horses(sound_str: str) -> List[int]:
    hooves = [int(i) for i in sound_str] # List of hoof sounds
    length = len(hooves)
    horses = []

    for i in range(length):
        sound = hooves[i]
        if sound != 0:
            horses += [i + 1] * sound
            index = i
            while index < length:
                hooves[index] -= sound
                index += i + 1


    return horses

print('Calculating Horses')
print(count_horses('0111020111'))
'''
0111020111
0010010010

should return [2, 3].
'''
