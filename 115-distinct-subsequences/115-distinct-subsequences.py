class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memoize = {}
        m, n = len(s), len(t)
        if m < n: return 0
        
        @lru_cache(None)
        def dp(i, j):
            if j == n:
                return 1
            elif i == m:
                return 0
            elif (i, j) in memoize:
                return memoize[(i, j)]
    
            # 3 choices: 
                # if the letter @ s[i] != t[j] -> then I move forward
                # if the letter @ s[i] == t[j] ->
                    # either pick the the b
                    # or not pick the pick
            
            totalSub = 0
            if s[i] != t[j]:
                totalSub += dp(i+1, j)
                
            elif s[i] == t[j]:
                notPicked = dp(i+1, j)
                picked = dp(i+1, j+1)
                totalSub += notPicked + picked
            
            memoize[(i, j)] = totalSub
            return totalSub
        
        
        return dp(0, 0)