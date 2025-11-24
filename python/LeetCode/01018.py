  def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
      n = len(nums)

      out = [0] * n
      running = 0

      for i in range(n):
          bit = nums[i]
          running = ((running << 1) + bit) % 5
          out[i] = running == 0
      
      return out
