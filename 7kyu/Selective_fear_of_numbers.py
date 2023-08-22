def am_I_afraid(day,num):
    if day == "Monday" and num == 12:
        return True
    elif day == "Tuesday" and num > 95:
        return True
    elif day == "Wednesday" and num == 34:
        return True
    elif day == "Thursday" and num == 0:
        return True
    elif day == "Friday" and num % 2 == 0:
        return True
    elif day == "Saturday" and num == 56:
        return True
    elif day == "Sunday" and (num == 666 or num == -666):
        return True
    
    return False