def flick_switch(lst):
    switch = True
    output = []
    for word in lst:
        if word == 'flick':
            switch = not switch
            output.append(switch)
        else:
            output.append(switch)
    
    return output