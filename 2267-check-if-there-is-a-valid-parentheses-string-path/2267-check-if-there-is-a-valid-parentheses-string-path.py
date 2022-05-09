class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        #bi directional bfs
        m, n = len(grid), len(grid[0])
        sq, eq = [], []
        START = (0, 0)
        END = (m-1, n-1)
        sv, ev = {(0, 0, 0): True}, {(m-1, n-1, 0): True}
        if (grid[0][0] == ")") or (grid[m-1][n-1] == "("): return False
        sq.append((START, self.getParaValue(grid[0][0])))
        eq.append((END, self.getParaValue(grid[m-1][n-1])))
        
        while sq and eq:
            sRC, sParaSum = sq.pop()
            sR , sC = sRC
            #Have to define the visited condition and define condition when meets eq
            for (sDR, sDC) in [(sR+1, sC), (sR, sC+1)]:
                
                if (0 <= sDR < m and 0 <= sDC < n and (sDR, sDC, sParaSum + self.getParaValue(grid[sDR][sDC])) not in sv):
                    currSParaSum = sParaSum + self.getParaValue(grid[sDR][sDC])
                    if currSParaSum < 0 or currSParaSum >= ((m*n)//2): continue
                    if (sR, sC, 0 - currSParaSum) in ev: 
                        #print(0-currSParaSum)
                        return True
                    
                    sq.append(((sDR, sDC), currSParaSum))
                    sv[(sDR, sDC, currSParaSum)] = True
            
            eRC, eParaSum = eq.pop()
            eR, eC = eRC
            for (eDR, eDC) in [(eR-1, eC), (eR, eC-1)]:
                
                if (0 <= eDR < m and 0 <= eDC < n and (eDR, eDC, eParaSum + self.getParaValue(grid[eDR][eDC])) not in ev):
                    currEParaSum = eParaSum + self.getParaValue(grid[eDR][eDC])
                    if currEParaSum > 0 or -currEParaSum >= (m*n)//2 : continue
                    if (eR, eC, 0 - currEParaSum) in sv: 
                        #print(sv, eDR, eDC, currEParaSum)
                        return True
                    eq.append(((eDR, eDC), currEParaSum))
                    ev[(eDR, eDC, currEParaSum)] = True
        
        
    
        return False
            
    
    def getParaValue(self, para):
        return 1 if para == "(" else -1