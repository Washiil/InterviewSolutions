def getKth(self, lo: int, hi: int, k: int) -> int:
		def pow_val(x: int) -> (int, int):
				steps = 0
				c = x
				while x != 1:
						if x % 2 == 0:
								x = x / 2
						else:
								x = 3 * x + 1
						steps += 1
				return (c, steps)
		
		pows = [pow_val(i) for i in range(lo, hi + 1)]
		pows.sort(key=lambda x: x[1])
		return pows[k - 1][0]