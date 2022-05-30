class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        question: is all the coin > 0
        can amount be <= 0?
        """
        
        if amount == 0: return 1
        
        dp = [1] + [0]*amount
        for coin in coins:
            for i, v in enumerate(dp):
                if v == 0 or i+coin >= len(dp): continue
                dp[i+coin] += dp[i]
            # -> [1, 1, 1, 1, 1, 1]
            # -> []

        
        return dp[-1]