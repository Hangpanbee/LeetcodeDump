class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        totalSq = m*n
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2: endSq = (r, c)
                elif grid[r][c] == 1: stSq = (r, c)
                elif grid[r][c] == -1: totalSq -= 1
        
        #why cant this question use cache?
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        cache = {}
        def dfs(r, c, sqWalked):
            #print(sqWalked, grid, r,c,endSq)
            if (r, c) == endSq and sqWalked == totalSq:
                return 1
            elif (r, c) == endSq:
                return 0
            #print(grid, sqWalked, r, c)
            path2 = 0
            for dr, dc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
 
                if 0 <= dr < m and 0 <= dc < n and (grid[dr][dc] == 0 or grid[dr][dc] == 2):
                    #if (r, c) == (0, 2): print(dr, dc)
                    prev = grid[dr][dc]
                    grid[dr][dc] = 3
                    path2 += dfs(dr,dc,sqWalked+1)
                    #print(path)
                    grid[dr][dc] = prev
            #cache[(r,c,sqWalked)] = path2
            #print(cache)
            return path2
            
            
        return dfs(stSq[0], stSq[1], 1)
        
            
        