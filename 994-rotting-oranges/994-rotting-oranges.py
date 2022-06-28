class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY_CELL = 0
        FRESH = 1
        ROTTEN = 2
        R, C = len(grid), len(grid[0])
    
        
        freshCount = 0
        q = collections.deque()
        for currR in range(R):
            for currC in range(C):
                if grid[currR][currC] == ROTTEN:
                    q.append((currR, currC , 0))
                elif grid[currR][currC] == FRESH:
                    freshCount += 1
        
        if freshCount == 0: return 0
        
        
        while q:
            currR, currC, mins = q.popleft()
            for dr, dc in {(currR+1, currC), (currR-1, currC), (currR, currC-1), (currR, currC+1)}:
                if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] == FRESH:
                    
                    q.append((dr, dc, mins+1))
                    grid[dr][dc] = ROTTEN
                    freshCount -= 1
                    if freshCount == 0: 
                        return mins+1
                    
        return -1
        