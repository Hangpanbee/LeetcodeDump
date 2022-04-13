class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0]*n for i in range(n)]
        
        
        d = 0
        pos = (0, 0)
        for num in range(1, n*n+1):

            currR, currC = pos
    
            matrix[currR][currC] = num
            
            dR, dC = directions[d%4]
            pos = (currR + dR, currC + dC) 
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= n or pos[1] >= n:
                d += 1
            elif matrix[pos[0]][pos[1]] != 0:
                d += 1
            dR, dC = directions[d%4]
            pos = (currR + dR, currC + dC) 
            
        return matrix
                        
            