class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        counter = {}
        max_num = 0
        for i in nums:
            max_num = max(max_num, i)
            if i in counter:
                counter[i] += i
            else:
                counter[i] = i
        
        
        if max_num < 2: return sum(nums)
        
        nums = sorted(list(counter.keys()))
       
        dp = [0] * (max_num+1)
        
        
        for i in range(max_num+1):
            if i <= 2:
                dp[i] = 0 if i not in counter else counter[i]
                continue
                
            if i not in counter:
                dp[i] = max(dp[i-2], dp[i-3])
            else:
                dp[i] = max(dp[i-2], dp[i-3])+counter[i]
  
        return max(dp[-1], dp[-2]) 
        
                    
     
            
        