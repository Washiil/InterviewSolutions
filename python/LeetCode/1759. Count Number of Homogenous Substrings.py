def countHomogenous(self, s: str) -> int:
		combos = 0
		cont = 0
		MOD = 10 ** 9 + 7

		for i in range(len(s)):
				if i == 0 or s[i] == s[i - 1]:
						cont += 1
				else:
						cont = 1
				
				combos = (combos + cont) % MOD
		
		return combos
