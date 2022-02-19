class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        row_copy = {}
        for i in range(n):
            row_copy[i] = matrix[i].copy()
        
        old_row = n-1
        for col in range(n):
            for row in range(n):
                matrix[row][col] = row_copy[old_row][row]
            old_row -= 1
        #print(matrix)
        return matrix
        