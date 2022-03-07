class Solution:
    def numWays(self, n: int, k: int) -> int:
        #if cur
  
        same_color, diff_color = 0, k
        for i in range(1, n):
            curr_diff_color = (same_color + diff_color)*(k-1)
            curr_same_color = (diff_color)
            same_color = curr_same_color
            diff_color = curr_diff_color
            #print(same_color, diff_color)
            
            
        return same_color + diff_color
        
        