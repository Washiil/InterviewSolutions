def findTheDifference(self, s: str, t: str) -> str:
		x = sorted(s)
		y = sorted(t)
		for i in range(0, len(y) - 1):
				if x[i] != y[i]:
						return y[i]
		return y[-1]