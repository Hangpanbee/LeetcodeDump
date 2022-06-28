class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        count0 = s.count('0')
        count1 = 0
        ans = float(inf)
        """
            0 1 0 1 1 0
            0 2 2 2 
        c1  0 1 1 2
        c0  2 2 1 1 
            0 0 0 0 0 0
            
        """
        if count0 == 0: return 0
        
        for i, v in enumerate(s):
          
            if v == "0":
                count0 -= 1
            elif v == "1":
                ans = min(ans, count0+count1)
                count1 += 1
                
        return min(ans, count1) if ans != float(inf) else 0
        
        