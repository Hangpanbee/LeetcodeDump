class Solution:
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.board = board    
        isStable = self.crush()
        while not isStable:
            self.gravity()
            isStable = self.crush()
        return self.board
        
    def gravity(self):
        board = self.board
        r, c = len(board), len(board[0])
        for cc in range(c):
            lr = r-1
            for rr in range(r-1, -1, -1):
                if board[rr][cc] > 0:
                    board[lr][cc] = board[rr][cc]
                    lr -= 1
            for lr in range(lr, -1, -1):
                board[lr][cc] = 0
        
        
        
    def crush(self):
        isStable = self._rowcrush() 
        isStable &= self._colcrush()
        return isStable
    
    
    def _rowcrush(self):
        board = self.board
        r, c = len(board), len(board[0])
        isStable = True
        for cr in range(r):
            for cc in range(c-2):
                if abs(board[cr][cc]) == abs(board[cr][cc+1]) == abs(board[cr][cc+2]) != 0:
                    board[cr][cc] = board[cr][cc+1] = board[cr][cc+2] = -abs(board[cr][cc])
                    
                    isStable = False

        return isStable
        
    
    def _colcrush(self):
        board = self.board
    
        r, c = len(board), len(board[0])
        isStable = True
        for cc in range(c):
            for cr in range(r-2):
                if abs(board[cr][cc]) == abs(board[cr+1][cc]) == abs(board[cr+2][cc]) != 0:
                    board[cr][cc] = board[cr+1][cc] = board[cr+2][cc] = -abs(board[cr][cc])
                    isStable = False
        return isStable