def tail_swap(strings):
    t1 = strings[0].split(':')
    t2 = strings[1].split(':')
    
    t1[1], t2[1] = t2[1], t1[1]
    return [':'.join(t1), ':'.join(t2)]