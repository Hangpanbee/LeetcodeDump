class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        countShip = 0
        for r in range(m):
            for c in range(n):
                if board[r][c] == "X":
                    countShip += 1
                    self.sinkShip(board, r, c)
                    #print(board)
        return countShip
        
    #set the initial cell to be sunk    
    def sinkShip(self, board, r, c):
        #print(r, c)
        shipD = -1
        m, n = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
        for d in range(4):
            dr, dc = r+directions[d][0], c+directions[d][1]
            if 0 <= dr < m and 0 <= dc < n and board[dr][dc] == "X":
                shipD = d
        if shipD == -1: return
        
        while 0 <= r < m and 0 <= c < n and board[r][c] == "X":
            board[r][c] = "."
            r+= directions[shipD][0]
            c+= directions[shipD][1]
            
        