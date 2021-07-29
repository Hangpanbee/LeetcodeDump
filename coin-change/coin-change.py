class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [99999] * (amount)
        
        for i in range(amount):
            
            for coin in coins:
                if (i + coin) > amount: continue
                dp[i + coin] = min(dp[i+coin], dp[i]+1)
 

        return dp[amount] if dp[amount] != 99999 else -1
            
        
        

            
        