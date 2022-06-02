class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        d = {}
        for r in range(m):
            d[(r, 0)] = matrix[r][0]
            
        for c in range(1, n):
            d[(0, c)] = matrix[0][c]
        
        for r in range(m):
            for c in range(n):
                if (r, c) in d: continue
                if r <= c:
                    if matrix[r][c] != d[(r-r, c-r)]: return False
                elif r > c:
                    if matrix[r][c] != d[(r-c, c-c)]: return False
                    
        return True
                    