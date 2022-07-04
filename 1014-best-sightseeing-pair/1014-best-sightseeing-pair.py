class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        forward = [0]*len(values)
        backward = [0]*len(values)
        
        """
            [8, 1, 5, 2, 6]
             0  7  6  5  6
             0  4  5  4  6     
        """
        
        
        for i, v in enumerate(values):
            prevVal = 0 if i - 1 < 0 else forward[i-1]-1
            if (i + 1) < len(values): forward[i+1] = v - 1
            forward[i] = max(prevVal, forward[i])
            

            
        ans = 0
        #print(forward, backward)
        for i, v in enumerate(values):
            ans = max(ans, v+forward[i])
            
            
        return ans
        