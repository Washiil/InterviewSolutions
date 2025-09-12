def doesAliceWin(self, s: str) -> bool:
    # Alice removes substr off vowels
    # Bob removes substr even vowels
    vowels = 'aeiou'

    if len([x for x in s if x in vowels]) == 0:
        return False

    return True
