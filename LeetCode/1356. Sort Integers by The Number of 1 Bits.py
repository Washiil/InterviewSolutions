# Full disclosure this is copied form the editorial on Leetcode. Clearly I need to touch up on my bit manipulation skills

def sortByBits(self, arr: list[int]) -> list[int]:
		def find_weight(num):
				mask = 1
				weight = 0
				
				while num:
						if num & mask:
								weight += 1
								num ^= mask
						
						mask <<= 1
				
				return weight
		
		arr.sort(key = lambda num: (find_weight(num), num))
		return arr