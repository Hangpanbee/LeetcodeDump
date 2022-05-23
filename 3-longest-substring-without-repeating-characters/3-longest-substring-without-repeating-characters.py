class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        uniqueMap = {}
        l, r = 0, 0
        
        maxAns = 0
        while r < len(s):
            
            while l < r and s[r] in uniqueMap:
                uniqueMap[s[l]] -= 1
                if uniqueMap[s[l]] == 0:
                    del uniqueMap[s[l]]
                l+=1
            maxAns = max(maxAns, r-l+1)
            uniqueMap[s[r]] = 1
            r+=1
        return maxAns
            
        
        
        