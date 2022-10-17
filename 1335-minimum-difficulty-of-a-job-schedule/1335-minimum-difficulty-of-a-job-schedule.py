class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        @lru_cache(None)
        def dp(i, d):
        
            if d == 0: return max(jobDifficulty[i:]) if i < len(jobDifficulty) else 0
            elif i == len(jobDifficulty): return float(inf)
            
            currMax = jobDifficulty[i]
            totalDiff = float(inf)
            for j in range(i, len(jobDifficulty)):
                
                currMax = max(currMax, jobDifficulty[j])
                totalDiff = min(currMax + dp(j+1, d-1), totalDiff)
                
            return totalDiff
        
        ans = dp(0, d)
        return ans if ans != float(inf) else -1