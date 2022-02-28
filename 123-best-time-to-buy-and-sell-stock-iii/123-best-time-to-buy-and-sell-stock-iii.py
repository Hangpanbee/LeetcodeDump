class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memoize = [0]*(len(prices)+1)
        curr_min = 99999999
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            memoize[i+1] = max(memoize[i], prices[i] - curr_min)
          
        one_pass_max = memoize[-1]
        memoize2 = [0]*(len(prices)+1)
        curr_max = 0
        second_pass_max = 0
        for i in range(len(prices)-1, -1, -1):
            
            curr_max = max(prices[i], curr_max)
            memoize2[i] = max(memoize2[i+1], curr_max - prices[i]) 
            second_pass_max = max(second_pass_max, memoize[i+1]+memoize2[i])
        #print(memoize, memoize2)
        return max(one_pass_max, second_pass_max)
                
                
            
            
        
        