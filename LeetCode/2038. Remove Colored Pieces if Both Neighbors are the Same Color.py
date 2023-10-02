def winnerOfGame(self, colors: str) -> bool:
		p1, p2 = 0, 0
		for i in range(1, len(colors) - 1):
				prev = colors[i-1]
				curr = colors[i]
				nxt = colors[i+1]
				if prev == curr == nxt:
						if curr == 'A':
								p1 += 1
						else:
								p2 += 1
		return p1 > p2