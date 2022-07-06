class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        """
            1   1   0
            0   0   1
            1   1   0
            
            1   1   0       1   1   0
            0   1   1       1   0   0 
            1   1   0       0   0   1
        """
        pattern1 = tuple(grid[0])
        pattern2 = []
        for i, v in enumerate(grid[0]):
            pattern2.append(1-v)
            
        pattern2 = tuple(pattern2)
        m, n = len(grid), len(grid[0])
        
        for r in range(m):
            currR = tuple(grid[r])
            
            if currR != pattern1 and currR != pattern2:
                return False
        
        return True
        