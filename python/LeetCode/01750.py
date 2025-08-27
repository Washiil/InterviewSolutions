def minimumLength(self, s: str) -> int:
    left = 0
    right = len(s) - 1

    while left < right and s[left] == s[right]:
        c = s[left]

        while left <= right and s[left] == c:
            left += 1
        
        while right > left and s[right] == c:
            right -= 1
        
    return (right - left) + 1