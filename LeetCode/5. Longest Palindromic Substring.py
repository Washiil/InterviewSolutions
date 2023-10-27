def longestPalindrome(self, s: str) -> str:
		def check(i, j):
				temp = s[i:j]
				return temp == temp[::-1]
		
		for end in range(len(s), 0, -1):
				for start in range(len(s) - end + 1):
						if check(start, start + end):
								return s[start:start + end]

		return ""