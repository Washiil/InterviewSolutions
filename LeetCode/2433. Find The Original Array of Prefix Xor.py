def findArray(self, pref: list[int]) -> list[int]:
		x = [pref[0]]
		for i in range(1, len(pref)):
				x.append(pref[i] ^ pref[i-1])
		return x