class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0, {(0,0)}))
        
      
        while heap:
            #print(heap)
            a = heapq.heappop(heap)
            h, r, c, visited = a
            if (r, c) == (n-1, n-1): return h
            #print(r, c, visited)
           
            for newR, newC in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                
                if 0 <= newR < n and 0 <= newC < n and (newR, newC) not in visited:
                    #visitedCopy = visited.copy()
                    visited.add((newR, newC))
                    #print(max(grid[newR][newC], h), newR, newC, visitedCopy)
                    # why this question does not need a copy of visited?
                    # because it is greedy?
                    heapq.heappush(heap, (max(grid[newR][newC], h), newR, newC, visited))
                  