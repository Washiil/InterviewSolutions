def countPalindromicSubsequence(self, s: str) -> int:
		result = 0
		unique = set(s)

		for letter in unique:
				i, j = s.index(letter), s.rindex(letter)

				between = set()

				for k in range(i + 1, j):
						between.add(s[k])
				
				result += len(between)
		
		return result