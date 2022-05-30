class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        is target always guarnateed to be found?
        or number be negative
        target can be less < 0
        """
        dp = [1] + [0]*target
      
        
        for i, v in enumerate(dp):
            for num in nums:
                if i + num >= len(dp): continue
                dp[i+num] += dp[i] 
        
        return dp[-1]
                
                