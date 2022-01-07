class Solution:
    def minCut(self, s: str) -> int:
        
        dp = [0] + [9999999] * len(s) + [999999]
        pali_tracker = {}
        
        
        for i in range(len(s)):
            
            odd_pali_l, odd_pali_r = self.isPali(i, i, s, dp)
            dp[odd_pali_r+1] = min(dp[odd_pali_l+1]+1, dp[odd_pali_r+1])
            if i+1 < len(s) and s[i] == s[i+1]: 
                even_pali_l, even_pali_r = self.isPali(i, i+1, s, dp)
                dp[even_pali_r+1] = min(dp[even_pali_l+1]+1, dp[even_pali_r+1])
                
            dp[i+1] = min(dp[i+1], dp[i]+1)
            
        #print(dp)
        return dp[-2]  - 1  
            
            
    def isPali(self, l , r, s, dp):
        
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            dp[r+1] = min(dp[l]+1, dp[r+1])
            l -= 1
            r += 1
        
        return l, r-1
        


        