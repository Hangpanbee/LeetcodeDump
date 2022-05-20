class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rMap = {}
        self.cMap = {}
        self.dMap = {1: 0, -1:0}
        self.rdMap = {}
        c = (n-1)
        for r in range(n):
            self.rdMap[(r, c)] = 0
            c-=1

    def move(self, row: int, col: int, player: int) -> int:
        player = -1 if player == 1 else 1
        self.rMap[row] = 1*player if row not in self.rMap else self.rMap[row] + 1*player
        self.cMap[col] = 1*player if col not in self.cMap else self.cMap[col] + 1*player
        if (row == col): self.dMap[1] += 1*player
        if (row, col) in self.rdMap: self.dMap[-1] += 1*player
        row = self.rMap[row] if abs(self.rMap[row])==self.n else 0
        col = self.cMap[col] if abs(self.cMap[col])==self.n else 0
        d1 = self.dMap[1] if abs(self.dMap[1]) == self.n else 0
        d2 = self.dMap[-1] if abs(self.dMap[-1]) == self.n else 0
        #print(row, col, d1, d2)
        win = row+col+d1+d2
        if (abs(win)) >= self.n:
            return 1 if win < 0 else 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)