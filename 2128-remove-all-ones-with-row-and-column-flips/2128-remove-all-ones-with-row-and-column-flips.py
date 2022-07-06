
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        match = grid[0]
        match_flip = [1 if x==0 else 0 for x in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != match and grid[i] != match_flip:
                return False
        return True