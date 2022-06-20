class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int[] dx = new int[] {1, 0,-1, 0};
        int[] dy = new int[] {0, 1, 0, -1};
        
        int m = matrix.length; int n = matrix[0].length;
        // m = 3; n = 3
        int i = 0;
        // i = 0
        List<Integer> ans = new LinkedList<>();
        // ans = [0,0,0,0,0,0,0,0,0]
        
        int cX = 0; int cY = 0;
        // cX = 0, cY = 0
        int cD = 0;
        // cD = 0
        while (i < (m*n)) {
            ans.add(matrix[cY][cX]);
            // ans = [1,0,0,0,0,0,0,0,0]
            // ans = [1,2,0,0,0,0,0,0,0]
            matrix[cY][cX] = -101;
            int nxtX = cX + dx[cD];
            //nxtX = 1, nxtY = 0
            //nxtX = 2, nxtY = 0
            int nxtY = cY + dy[cD];
            //System.out.println(nxtX);
            //System.out.println(nxtY);
            //System.out.println("HELLO");
            while (nxtX < 0 || nxtX >= n || nxtY < 0  || nxtY >= m || matrix[nxtY][nxtX] == -101) {
                if (i == m*n-1) break;
                cD += 1;
                cD %= 4;
                nxtX = cX + dx[cD];
                nxtY = cY + dy[cD];
            };
            cX = nxtX; cY = nxtY;
            i++;
            //i = 1
        }
        
        return ans;
        
        
        
    }
}