class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set([amount])
        while q:
            accum_amount, num_coins = q.popleft()
            if accum_amount == 0:
                    return num_coins
            for coin in coins:
                if accum_amount - coin >= 0 and accum_amount - coin not in seen:
                    q.append((accum_amount - coin, num_coins + 1))
                    seen.add(accum_amount - coin)

        return -1
        

            
        