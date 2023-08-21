def is_interesting(number, awesome_phrases):
    for i in range(3):
        output = 2 if i == 0 else 1
        num = number + i
        return 0


def is_incr(num):
    pass


def is_decr(num):
    pass
    
def is_palindrome(num):
    return True if str(num) == str(num)[::-1] else False

def all_zeros(num):
    return True if len([c for c in [*str(num)[1:]] if c != '0']) == 0 else False


def is_awesome(num, awesome_phrases):
    return True if num in awesome_phrases else False
