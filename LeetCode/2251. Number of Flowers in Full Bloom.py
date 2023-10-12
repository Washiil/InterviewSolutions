def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
		big = max(people)
		frame = []
		for flower in flowers:
				start = flower[0]
				if start > big:
						continue
				end = flower[1] + 1
				if end > len(frame): # make space for new things
						frame.extend([0] * (end - len(frame)))
				
				for i in range(start, end):
						frame[i] = frame[i] + 1
				print(len(frame), frame)

		return [frame[p] if p < len(frame) else 0 for p in people]

# Currently a memory error because its a bit of a brute force approach. I plan to come back and revise later