class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R, self.C = len(grid), len(grid[0])

        noIslands = 0
        for cr in range(self.R):
            for cc in range(self.C):
                if grid[cr][cc] == "0": continue
                noIslands += 1
                grid[cr][cc] = "0"
                self.dfs(grid, cr, cc)
        
        return noIslands
        
        
    def dfs(self, grid, cr, cc):
        
        
        for nxtR, nxtC in ((cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)):
            if 0 <= nxtC < self.C and 0 <= nxtR < self.R and grid[nxtR][nxtC] == "1":
                grid[nxtR][nxtC] = "0"
                self.dfs(grid, nxtR, nxtC)