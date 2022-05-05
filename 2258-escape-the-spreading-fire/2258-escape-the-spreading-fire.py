class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        FIRE = 1
        WALL = 2
        fireMap = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == FIRE:
                    q.append((r, c, 1))
                    
                if grid[r][c] == WALL:
                    grid[r][c] = 100000000
                    fireMap[(r, c)] = True
        WALL = 100000000           
  
        while q:
            r,c,t = q.popleft()
            fireMap[(r, c)] = True
            for dr, dc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] < 1:
                    grid[dr][dc] = t+1    
                    fireMap[(dr, dc)] = True
                    q.append((dr, dc, t+1))
 
        #if len(fireMap)+1 < len(grid)*len(grid[0]): return 1000000000
        
        heap = []
        time = 1
        heapq.heappush(heap, (-grid[0][0]-time, 0, 0, 1, grid[0][0]-time))
        
        visited = {(0,0): True}
        while heap:
            diff, r, c, t, globalDiff = heapq.heappop(heap)
            diff = -diff
            t += 1
   
            for dr, dc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                
                if (dr, dc) == (m-1, n-1) and (grid[dr][dc] == 0 or t <= grid[dr][dc]):
                    ans = min(diff-1, grid[dr][dc] - t) 
                    return ans if ans >= 0 else 1000000000
                
                if 0 <= dr < m and 0 <= dc < n and grid[dr][dc] != 100000000 and (dr, dc) not in visited and (grid[dr][dc] == 0 or t < grid[dr][dc]):
                    heapq.heappush(heap, (min(grid[dr][dc]-t, diff) * (-1), dr, dc, t, min(globalDiff, grid[dr][dc]-t) ) )
                    visited[(dr, dc)] = True
            
        return -1