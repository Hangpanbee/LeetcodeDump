class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        """
        why dp does work here?
        why need a visisted set here?
        """
        dp = [[0]*n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if (r, c) == (0,0): continue
                right = float(inf) if c-1 < 0 else grid[r][c-1]
                down = float(inf) if r-1 < 0 else grid[r-1][c]
                grid[r][c] += min(right, down)
        
        #print(grid)
        return grid[m-1][n-1]