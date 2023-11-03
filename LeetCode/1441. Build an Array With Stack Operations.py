def buildArray(self, target: list[int], n: int) -> list[str]:
		result = []

		for i in range(1, n + 1):
				if i in target:
						result.append("Push")
				else:
						result.extend(["Push", "Pop"])
				if i == target[-1]:
						break
		return result