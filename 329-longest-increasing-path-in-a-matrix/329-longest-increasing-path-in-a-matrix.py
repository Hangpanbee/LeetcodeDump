class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # why adding a visited dict works here?????
        
        # ans: how to notfiy the current cell of its parents? can use 0 for parent, or pass parent down
        
        # PAY ATTENTION TO THE LOCATION OF LOGIC, WHERE TO PUT MEMOIZE LOGIC
        matrixRow, matrixCol = len(matrix), len(matrix[0])
        memoize = {}
        visited = {}
        def dfs(row, col, r, c, val):
            if row < 0 or col < 0 or row >= matrixRow or col >= matrixCol:
                return 0
            

            if (row, col) != (r, c) and matrix[row][col] >= val:
                return 0
            
            if (row, col) in memoize: return memoize[(row, col)]
            
            currVal = matrix[row][col]
            
            #left =  dfs(row, col - 1, currVal)
            up = dfs(row - 1, col, row, col, currVal)
            down =  dfs(row + 1, col, row, col, currVal)
            left =  dfs(row, col - 1, row, col, currVal)
            right = dfs(row, col + 1, row, col, currVal)
            memoize[(row, col)] = 1 + max(left, down, up, right)
            return memoize[(row, col)]
        
        ans = 0
        for r in range(matrixRow):
            for c in range(matrixCol):
                ans = max(ans,  dfs(r, c, r, c, matrix[r][c]))

            
        return ans 