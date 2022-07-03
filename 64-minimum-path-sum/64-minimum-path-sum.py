class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        """
        why dp does work here?
        why need a visisted set here?
        """
        heap = []
        heapq.heappush(heap, (grid[0][0], 0,0) )
        visited = {}
        visited[(0,0)] = True
        
        while heap:
            pathSum, currR, currC = heapq.heappop(heap)
            if (currR, currC) == (m-1, n-1):
                return pathSum 
            
            for nxtR, nxtC in ((currR+1, currC), (currR, currC+1)):
                if 0 <= nxtR < m and 0 <= nxtC < n and (nxtR, nxtC) not in visited:
                    visited[(nxtR, nxtC)] = True
                    heapq.heappush(heap, (pathSum+grid[nxtR][nxtC], nxtR, nxtC))
                    
        
        return -1