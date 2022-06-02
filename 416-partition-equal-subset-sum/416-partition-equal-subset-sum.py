class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # why can't this question be greedy:
        # [1,1,5,6,11]
        
        totalSum = sum(nums)
        if totalSum%2==1: return False
        
        goal = totalSum//2 
        
        dp = [True] + [False]*goal
  
        for k, num in enumerate(nums):
            for j in range(goal,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
            #print(dp, num)
    
        print(dp)
        return dp[-1] 