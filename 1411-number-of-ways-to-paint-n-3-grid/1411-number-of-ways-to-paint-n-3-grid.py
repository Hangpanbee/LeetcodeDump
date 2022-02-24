class Solution:
    def numOfWays(self, n: int) -> int:
        row_xyx = 6
        row_xyz = 6
        m = 10**9+7
        for i in range(1, n):
            curr_xyx = 3*row_xyx + 2*row_xyz
            curr_xyz = 2*row_xyx + 2*row_xyz
            row_xyx = curr_xyx
            row_xyz = curr_xyz
        
        return (row_xyx + row_xyz)%m