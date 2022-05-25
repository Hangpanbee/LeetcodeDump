class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        dp = [[0]*(len(text1)+1) for i in range(len(text2)+1)]
        ans = 0
        
        for i2, v2 in enumerate(text2):
            for i, v in enumerate(text1):
                if v == v2:
                    dp[i2+1][i+1] = max(dp[i2][i]+1, dp[i2+1][i+1])
                else:
                    dp[i2+1][i+1] = max(dp[i2+1][i], dp[i2][i+1])
                ans = max(ans, dp[i2+1][i+1]) 
        #print(dp)
        return ans