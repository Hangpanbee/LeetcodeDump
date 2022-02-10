class Solution:
    def maxProfit(self, K: int, prices: List[int]) -> int:
        memoize = {}
        
        @lru_cache(None)
        def helper(k, index, isBought):
            if k >= K or index == len(prices):
                return 0
            if (k, index, isBought) not in memoize:
                sell = noSell = buy = noBuy = 0
                if isBought:
                    #continue to hold or sell
                    sell =  prices[index] + helper(k+1, index+1, False)
                    noSell = helper(k, index+1, True)

                elif not isBought:
                    #buy or do nothing
                    buy = helper(k, index+1, True) - prices[index]
                    noBuy = helper(k, index+1, False)
                memoize[(k, index, isBought)] = max(sell, noSell, buy, noBuy)
            return memoize[(k, index, isBought)]
            
              
                
        return helper(0, 0, False)

            
                
            
                
        