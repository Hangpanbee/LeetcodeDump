class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memoiz = {}
        def dp(row, col):
            if row == (len(matrix)-1) and col >= 0 and col < len(matrix[0]): return matrix[row][col]
            elif (row, col) in memoiz: return memoiz[(row, col)]
            elif row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
                return 999999
            
            
            memoiz[(row, col)] = matrix[row][col] + min(dp(row+1, col-1), dp(row+1, col), dp(row+1, col+1))
            return memoiz[(row, col)]
         
        min_ans = 9999999
        for col in range(len(matrix[0])):
            curr_min = dp(0, col)

            min_ans = min(min_ans, curr_min)
        #print(memoiz)   
        return min_ans
            
        