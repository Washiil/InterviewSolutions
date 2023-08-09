def count_smileys(arr):
    eyes = [':', ';']
    noses = ['-', '~']
    mouths = [')', 'D']
    total = 0
    for smile in arr:
        if smile[0] not in eyes:
            continue
        if len(smile) > 2:
            if smile[1] not in noses:
                continue
            if smile[2] not in mouths:
                continue
        else:
            if smile[1] not in mouths:
                continue
                
        total += 1
    return total