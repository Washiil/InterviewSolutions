def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
		delta = []
		for i in range(len(dist)):
				delta.append(dist[i] / speed[i])
		
		delta.sort()
		monsters = 0

		for i in range(len(delta)):
				if delta[i] <= i:
						break
				
				monsters += 1
		
		return monsters
