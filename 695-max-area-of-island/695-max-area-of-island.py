class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(currR, currC):
            currArea = 0
            for nxtR, nxtC in ((currR+1,currC), (currR-1, currC), (currR, currC+1), (currR, currC-1)):
                if 0 <= nxtR < R and 0 <= nxtC < C and grid[nxtR][nxtC] == 1:
                    grid[nxtR][nxtC] = "#"
                    currArea += 1 + dfs(nxtR, nxtC)
                
            return currArea
        
        maxArea = 0
        for currR in range(R):
            for currC in range(C):
                if grid[currR][currC] == 1:
                    grid[currR][currC] = "#"
                    maxArea = max(1+dfs(currR, currC), maxArea)
                    
        return maxArea
        
        