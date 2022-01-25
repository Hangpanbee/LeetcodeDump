class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        matrix_copy = [[(0, 0, 0, 0)]*(col+1) for i in range(row+1)]
        ans = 0
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 1:
                    new_row = matrix_copy[r+1][c][0] + 1
                    new_col = matrix_copy[r][c+1][1] + 1
                    new_diag = matrix_copy[r][c][2] + 1
                    if c+2 < (col+1): new_anti = matrix_copy[r][c+2][3] + 1
                    else: new_anti = 0
                    ans = max(ans, new_row, new_col, new_diag, new_anti)
                    matrix_copy[r+1][c+1] = (new_row, new_col, new_diag, new_anti)
                    
        return ans
            