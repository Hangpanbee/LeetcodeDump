class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        WILL_DIE = 2
        WILL_REVIVE = -2
        rowBoard, colBoard = len(board), len(board[0])
        
        def nextState(r, c):
            up = 0 if r-1 < 0 else max(board[r-1][c], 0)
            up = 1 if up == 2 else up
            down = 0 if r+1 >= rowBoard else board[r+1][c]
            left = 0 if c-1 < 0 else max(board[r][c-1], 0)
            left = 1 if left == 2 else left
            right = 0 if c+1 >= colBoard else board[r][c+1]
            ul = 0 if r-1 < 0 or c-1 < 0 else max(board[r-1][c-1], 0)
            ul = 1 if ul == 2 else ul
            ur = 0 if r-1 < 0 or c+1 >= colBoard else max(board[r-1][c+1], 0)
            ur = 1 if ur == 2 else ur
            dl = 0 if r+1 >= rowBoard or c-1 < 0 else board[r+1][c-1]
      
            dr = 0 if r+1 >= rowBoard or c+1 >= colBoard else board[r+1][c+1]
            
            
            totalNeighbors = up + down + left + right + ul + ur + dl + dr
            return totalNeighbors
        
        
        for r in range(rowBoard):
            for c in range(colBoard):
                if board[r][c] == 0:
                    board[r][c] = WILL_REVIVE if nextState(r, c) == 3 else 0
                elif board[r][c] == 1:
                    board[r][c] = WILL_DIE if nextState(r, c) < 2 or nextState(r, c) > 3  else 1
                    
        for r in range(rowBoard):
            for c in range(colBoard):
                if board[r][c] == WILL_DIE:
                    board[r][c] = 0
                elif board[r][c] == WILL_REVIVE:
                    board[r][c] = 1
        
        return board