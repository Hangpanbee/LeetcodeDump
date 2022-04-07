class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            new_stone = stones[-1]-stones[-2]
            stones.pop()
            stones.pop()
            if new_stone != 0: stones.append(new_stone)
            else: continue
        return stones[0] if len(stones) > 0 else 0
            
            
        