def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
		@lru_cache(None)
		def dp(row, ssum):
				if row == m:
						return abs(ssum - target)
				
				ans = sys.maxsize
				for num in mat[row]:
						ans = min(ans, dp(row + 1, ssum + num))
						if (ssum + num) >= target:
								break
				
				return ans
		
		m = len(mat)

		for i in range(m):
				mat[i] = sorted(set(mat[i]))
		
		return dp(0, 0)