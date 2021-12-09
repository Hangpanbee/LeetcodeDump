class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        #[min_val, max_val]
        dp = [[0,0]] + [[float(-inf), float(inf)]] * len(nums)
        #print(dp)
        max_val = 0
        for i in range(len(nums)):
            #min_val
            a = min(dp[i][0]*nums[i], dp[i][1]*nums[i])
            b = max(dp[i][0]*nums[i], dp[i][1]*nums[i])
            
            
            dp[i+1] = [min(a, nums[i]), max(b, nums[i])]
            max_val = max(dp[i+1][1], max_val)
        print(dp)   
        return max_val
        