class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        LAND = 1
        WATER = 0
        
        row, col = len(grid), len(grid[0])
        seenIsland = {}
        directions = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
        
        def dfs(r, c):
            path = ""
            for k, v in directions.items():
                #print(path)
                dr, dc = v
                nxtR = r + dr
                nxtC = c + dc
                if 0 <= nxtR < row and 0 <= nxtC < col and grid[nxtR][nxtC] == LAND:
                    grid[nxtR][nxtC] = WATER
                    path += k + dfs(nxtR, nxtC) + "-"
           
            return path
            
        numOfDIsland = 0 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == LAND:
                    numOfDIsland += 1
                    # -> r,c = (0, 0) -> numOfDisland = 1
                    path = dfs(r, c)
                   
                    if path in seenIsland:
                        numOfDIsland -= 1
                    seenIsland[path] = True
        #print(len(seenIsland))
        return numOfDIsland
    
 
        
        