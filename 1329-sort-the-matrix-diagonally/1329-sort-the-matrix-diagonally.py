class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        R, C = len(mat), len(mat[0])
        
        diag = collections.defaultdict(list)
        for cr in range(R):
            for cc in range(C):
                diag[cc-cr].append(mat[cr][cc])
                
        for diagId, diagVals in diag.items():
            diagVals.sort()

        for cr in range(R):
            for cc in range(C):
                mat[cr][cc] = diag[cc-cr].pop(0)
                
        return mat