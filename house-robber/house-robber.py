class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
      
        return max(dp[-1], dp[-2])
        