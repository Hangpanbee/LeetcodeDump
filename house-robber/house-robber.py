class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            if i < 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
      
        return max(dp[-1], dp[-2])
        