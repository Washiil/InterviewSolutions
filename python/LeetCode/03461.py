# Lovely counting approach https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/solutions/7293347/from-brute-force-to-o-n-3-solutions-with-gradual-optimizations/

def hasSameDigits(self, s: str) -> bool:
    lst = [int(v) for v in s]
    n = len(lst)
    binomial_coeff = [comb(n-2,i) for i in range(n-1)] 
    left = sum([digit*coeff for digit, coeff in zip(lst[:-1], binomial_coeff)]) % 10
    right = sum([digit*coeff for digit, coeff in zip(lst[1:], binomial_coeff)]) % 10

    return left == right