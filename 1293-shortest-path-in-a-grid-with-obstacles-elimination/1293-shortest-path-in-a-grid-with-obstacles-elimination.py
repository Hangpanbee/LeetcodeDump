class Solution:
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        WALL = 1
        
        q = []
        heapq.heappush(q, (0, 0, 0, K))
        visited = set()
        
        while q:
            steps, r, c, k = heapq.heappop(q)
            if (r, c) == (m-1, n-1): return steps
            
            for dr, dc in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                if 0 <= dr < m and 0 <= dc < n:
                    dk = k
                    if grid[dr][dc] == WALL:
                        if k == 0: continue
                        dk -= 1
                    if (dr, dc, dk) in visited: continue
                    #visitedCopy = visited.copy()
       
                    #if (dr, dc) == (m-1, n-1): return steps+1
                    visited.add((dr, dc, dk))
                    heapq.heappush(q, (steps+1, dr, dc, dk))
            
        return -1 