class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:

        
        for pile in range(len(piles)):
            for i in range(len(piles[pile])):
                if i > 0:
                    piles[pile][i] += piles[pile][i-1]
        #print(piles, len(piles))
        @lru_cache(None)
        def dp(i, k):
            if i == len(piles):
                if k == 0: return 0
                else: return 0
            
            curr_val = dp(i+1, k)
            ans = -1
            for index in range(min(k, len(piles[i]))):
                ans = max(ans, piles[i][index] + dp(i+1, k - index - 1))
            #print(i, k, curr_val, ans)    
            return max(ans, curr_val)
                

                
        return dp(0, K)
        