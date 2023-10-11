def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		ana_map = {}
		for word in strs:
				parsed = ''.join(sorted(word))
				if parsed in ana_map.keys(): ana_map[parsed].append(word)
				else: ana_map[parsed] = [word]

		return list(ana_map.values())