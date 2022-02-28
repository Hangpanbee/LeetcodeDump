class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memoize = {}
        
        def helper(row, cell):
 
            if row == 0:
                return 1
            elif row == 1:
                return 1
            
            if (row, cell) in memoize:
                return memoize[(row, cell)]
            
            
            if (cell-1) == 0:
                memoize[(row-1, 0)] = 0
            else:
                memoize[(row-1, cell-1)] = helper(row-1, cell-1)
            
            if (cell) >= (row+1):
                memoize[(row-1, cell)] = 0
            else:
                memoize[(row-1, cell)] = helper(row-1, cell)

            memoize[(row, cell)] = memoize[(row-1, cell-1)] + memoize[(row-1, cell)]
            return memoize[(row, cell)]
        
        ans = []  
        for i in range(rowIndex+1):

            ans.append(helper(rowIndex, i+1))
            
        return ans
        