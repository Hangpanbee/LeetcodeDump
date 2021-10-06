class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [nums[0]] + [0]*(len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i]+dp[i-1], nums[i])
        return max(dp)
        