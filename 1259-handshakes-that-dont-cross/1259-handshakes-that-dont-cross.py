class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = [1,1,2,5] + [0] * (numPeople//2-3)
        if (numPeople // 2) <= 3: return dp[numPeople//2]
        pair = numPeople//2 

        for i in range(4, pair + 1):
            r = i
            for j in range((i+1)//2):
                if (r-1) != j:
                    dp[i] += dp[r-1]*dp[j]*2
                else:
                    dp[i] += dp[r-1]*dp[j]
    
                r -= 1
        
        
        return dp[-1] % (10**9+7)