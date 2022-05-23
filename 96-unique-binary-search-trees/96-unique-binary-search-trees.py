class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+3)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if n <= 3: return dp[n]
        
        for i in range(4, n+1):
            
            for way in range(1, i//2+1):
                dp[i] += dp[i-way]*dp[max(way-1, 0)]*2 
            if i%2==1:
                dp[i] += dp[i//2]*dp[i//2]
        #print(dp)
        return dp[n]