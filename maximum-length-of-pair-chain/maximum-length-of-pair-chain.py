class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [-99999999] + len(pairs) * [999999]
        dp_target = 0
        #print(pairs)
        for left, right in pairs:
            
            if dp[dp_target] < left:
                dp_target += 1
                dp[dp_target] = min(dp[dp_target], right)
            else:
                l, h = 1, dp_target
                while l < h:
                    m = l + (h-l)//2
                    if left > dp[m]:
                        l = m + 1
                    elif left <= dp[m]:
                        h = m 
                dp[l] = min(dp[l], right)
        #print(dp)      
        return dp_target
                        
                
            
        