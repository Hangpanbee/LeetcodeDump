class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and n == 1: return 1 if obstacleGrid[0][0] == 0 else 0
        if obstacleGrid[0][0] == 1: return 0
        
        @lru_cache(None)
        def dfs(currR, currC):
            if (currR, currC) == (m-1, n-1):
                return 1
  
            totalPath = 0
            for dr, dc in ((currR+1, currC), (currR, currC+1)):
                if 0 <= dr < m and 0 <= dc < n and obstacleGrid[dr][dc] == 0:
                    obstacleGrid[dr][dc] = 2
                    totalPath += dfs(dr, dc)
                    obstacleGrid[dr][dc] = 0
                
            #print(totalPath, currR, currC)
            return totalPath
        
        obstacleGrid[0][0] = 1
        return dfs(0, 0)