class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        curr_max = [0]*(len(prices)+1)  
        buy = [-9999999]*(len(prices)+1)
            
        for i, v in enumerate(prices):
            prev_sum = 0
            if i-2 >= 0:
                prev_sum = curr_max[i-1]
            buy[i+1] = max(buy[i], -v+prev_sum) 
            curr_max[i+1] = max(curr_max[i], v + buy[i])
    
        return curr_max[-1]
            
        