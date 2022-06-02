class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ALICE = 1
        BOB = -1
        @lru_cache(None)
        def dp(i, j, turn):
            if i > j: return 0 
            
            if turn == ALICE:
                left = piles[i] + dp(i+1, j, BOB)
                right = piles[j] + dp(i, j-1, BOB)
                return max(left, right)
            elif turn == BOB:
                left = dp(i+1, j, ALICE) - piles[i]
                right = dp(i, j-1, ALICE) - piles[j]
                return min(left, right)
            
        finalScore = dp(0, len(piles)-1, ALICE)
       
        return True if finalScore > 0 else False