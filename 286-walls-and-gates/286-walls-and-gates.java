class Solution {
    public void wallsAndGates(int[][] rooms) {
        int INF = Integer.MAX_VALUE;
        int GATE = 0;
        int WALL = -1;
        Queue<int[]> q = new LinkedList<>();
        
        for (int row=0; row < rooms.length; row++) {
            for (int col=0; col < rooms[0].length; col++) {
                if (rooms[row][col] == GATE)
                    q.add(new int[] {row, col, 0} );
            };
        };
        
        int[] dcol = {1, -1, 0, 0};
        int[] drow = {0, 0, 1, -1};
        while (!q.isEmpty()) {
            int[] curr = q.remove();
            int row = curr[0];
            int col = curr[1];
            int dist = curr[2];
            
            for (int count = 0; count < 4; count++) {
                int new_row = row + drow[count];
                int new_col = col + dcol[count];
                
                if (new_row < 0 || new_col < 0 || new_row >= rooms.length || new_col >= rooms[0].length) {
                    continue;
                } else if (rooms[new_row][new_col] == INF) {
                    rooms[new_row][new_col] = dist+1;
                    q.add(new int[] {new_row, new_col, dist+1});
                };
                
                
            };
            
        };
        
        
    };
    
    
}