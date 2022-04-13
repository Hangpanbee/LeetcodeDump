class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];
        int[][] ds = {{0,1},{1,0},{0,-1},{-1,0}};

        int d = 0;
        int r = 0; int c = 0;
        for (int i = 1; i < (n*n+1); i++) {
            ans[r][c] = i;


            if (r + ds[d][0] < 0 || r + ds[d][0] >= n || c + ds[d][1] < 0 || c+ds[d][1] >=n || ans[r+ds[d][0]][c+ds[d][1]] != 0) {
                d = (d+1)%4;
            };
            r += ds[d][0];
            c += ds[d][1];
            
        };
        
        return ans;
        
        
    }
}