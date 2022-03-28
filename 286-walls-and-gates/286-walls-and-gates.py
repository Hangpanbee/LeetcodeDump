class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1
        GATE = 0
        WALL = -1
        q = collections.deque()
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(q):
            while q:
                row, col, dist = q.popleft()
                for add_row, add_col in directs:
                    new_row = row + add_row
                    new_col = col + add_col
                    if new_row < 0 or new_col < 0 or new_row >= len(rooms) or new_col >= len(rooms[0]):
                        continue
                    elif rooms[new_row][new_col] == INF:
           
                        rooms[new_row][new_col] = min(rooms[new_row][new_col], dist+1)
                        q.append([new_row, new_col, dist+1])
                        
                
            
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == GATE:
                    q.append([row, col, 0])
                    
        if q:
            bfs(q)

        return rooms