def billboard(name, price=30):
    total=0
    for c in name:
        total += price
    return total