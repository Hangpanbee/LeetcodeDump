class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flattenGrid = len(grid)*len(grid[0])
        k = k % flattenGrid
        if k == 0: return grid
        
        
        #preprocessed
        for r in range(len(grid)):
            self.inPlaceReverse(grid[r], 0, len(grid[r])-1)
   
        
        for r in range(len(grid)//2):
            grid[r], grid[len(grid)-r-1] = grid[len(grid)-r-1], grid[r]
        
        l, r = k, flattenGrid - 1
        self.inPlaceReverse2(l, r, grid)
        self.inPlaceReverse2(0, k-1, grid)
       
        return grid
    
    def inPlaceReverse(self, row, l, r):
        
        while l < r:
            row[l], row[r] = row[r], row[l]
            l += 1
            r -= 1
            
    def inPlaceReverse2(self, l, r, grid):
        while l < r:
            row_l, row_r = l//len(grid[0]), r//len(grid[0])
            col_l, col_r = l%len(grid[0]), r%len(grid[0])
            #print(row_l, row_r, col_l, col_r)
            grid[row_l][col_l], grid[row_r][col_r] = grid[row_r][col_r], grid[row_l][col_l]
            
            l += 1
            r -= 1
       
        