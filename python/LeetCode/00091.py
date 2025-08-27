# I should come back and review this one as the dynamic programming approach is not intuitive to me

def numDecodings(self, s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    # Initialize dp with one longer than the len of s
    dp = [0] * (n + 1)
    # Initialize first two values
    dp[0] = 1
    dp[1] = 1

    # Skip first two numbers and then go to the end of the array + 1
    for i in range(2, n + 1):
        # Parse first digit
        one_digit = int(s[i - 1])
        # Parse out the double of the digits
        two_digits = int(s[i - 2:i])

        # Kind of makes sense now
        if one_digit != 0:
            dp[i] += dp[i - 1]

        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]
