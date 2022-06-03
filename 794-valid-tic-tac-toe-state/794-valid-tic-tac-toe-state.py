class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        
        
        xCount = sum(board[row][cell] == "X" for row in range(3) for cell in range(3))
        oCount = sum(board[row][cell] == "O" for row in range(3) for cell in range(3))
        isTurnTaken = xCount == oCount or (xCount-1) == oCount
        
        rowMap = {0: 0, 1:0, 2:0}
        colMap = {0: 0, 1:0, 2:0}
        diagMap = {1: 0, -1:0}
        
        prevWin = [0, 0, 0, 0]
     
        winCount = 0
        for row in range(3):
            for col in range(3):
                
                if board[row][col] == "X": turn = 1
                elif board[row][col] == "O": turn = -1
                elif board[row][col] == " ": continue
                
                rowMap[row] += turn
                colMap[col] += turn
                
                isLDiag = True if row == col else False
                isRDiag = True if row+col == 2 else False
                if isLDiag: diagMap[1] += turn
                if isRDiag: diagMap[-1] += turn
                
                if rowMap[row] == turn*3:
                    if prevWin[0]: return False
                    prevWin[0] = turn
                if colMap[col] == turn*3:
                    if prevWin[1]: return False
                    prevWin[1] = turn
                if isLDiag and diagMap[1] == turn*3:
                    if prevWin[2]: return False
                    prevWin[2] = turn
                if isRDiag and diagMap[-1] == turn*3:
                    if prevWin[3]: return False
                    prevWin[3] = turn
                
            
        #print(prevWin)
        winner = 0
        for pW in prevWin:
            if abs(pW) >= 2: return False
            if pW == 1:
                winner = 1
            elif pW == -1:
                winner = -1
        
        #print(winner, (winner == 1 and oCount+1 == xCount) or (winner==-1 and xCount == oCount))
        isTurnTaken = isTurnTaken and ((winner == 1 and oCount+1 == xCount) or (winner==-1 and xCount == oCount) or winner == 0)
        
        
        
        
        return isTurnTaken