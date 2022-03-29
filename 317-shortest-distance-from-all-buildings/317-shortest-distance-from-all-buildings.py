class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def isReachable(row, col):
            left = False if row - 1 < 0 else grid[row-1][col] == 0
            right = False if row + 1 >= len(grid)  else grid[row+1][col] == 0
            up = False if col - 1 < 0 else grid[row][col-1] == 0
            down = False if col + 1 >= len(grid[0]) else grid[row][col+1] == 0
            return left or right or up or down
        
        q = collections.deque()
        i = 0
        visited = {}
        for row in range(len(grid)):   
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if not isReachable(row, col): return -1
                    q.append((row, col, i))
                    grid[row][col] = 100000
                    visited[(row, col, i)] = grid[row][col]                    
                    i += 1
                elif grid[row][col] == 2:
                    grid[row][col] = -200000

                             
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        reachable = (i)*100000
        ans = 9999999999999
        while q:
            row, col, house_ith = q.popleft()
            if grid[row][col] > reachable:
                ans = min(ans, grid[row][col] - reachable)

            for r, c in directs:
                new_row = row + r
                new_col = col + c
                
                if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                    continue
                elif grid[new_row][new_col] == 100000 or grid[new_row][new_col] == -200000:
                    continue
                elif (new_row, new_col, house_ith) in visited:
                    continue
                visited[(new_row, new_col, house_ith)] = visited[(row, col, house_ith)] + 1
                grid[new_row][new_col] += visited[(new_row, new_col, house_ith)]
                q.append((new_row, new_col, house_ith))
                

        
        return ans if ans != 9999999999999 else -1