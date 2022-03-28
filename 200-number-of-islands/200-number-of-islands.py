class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def bfs(curr_row, curr_col):
            q = collections.deque()
            q.append([curr_row, curr_col])
            grid[curr_row][curr_col] = "0"
            while q:
                row, col = q.popleft()
                grid[row][col] = "0"
                for new_row, new_col in directs:
                    next_row = row + new_row
                    next_col = col + new_col
                    if next_row < 0 or next_col < 0 or next_row >= len(grid) or next_col >= len(grid[0]):
                        continue  
                    if grid[next_row][next_col] == "0":
                        continue
                    grid[next_row][next_col] = "0"
                    q.append([next_row, next_col])
                
        ans = 0            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    #print(row, col, visited)
                    bfs(row, col)
                    ans += 1
                    
        return ans