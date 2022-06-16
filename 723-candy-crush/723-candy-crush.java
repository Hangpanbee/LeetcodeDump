class Solution {
    public int[][] candyCrush(int[][] board) {
        boolean isRowStable = candyMatchRow(board);
        boolean isColStable = candyMatchCol(board);
        updateBoard(board);
        boolean isStable = isRowStable && isColStable;
        while (!isStable) {
            isRowStable = candyMatchRow(board);
            isColStable = candyMatchCol(board);
            updateBoard(board);
            isStable = isRowStable && isColStable;
        }
        return board;
    }
    
    public void updateBoard(int[][] board) {
        int row = board.length; int col = board[0].length;
        //Careful drop at the upmost corner
        // 2 pointers have to go from the bottom first
        for (int cc = 0; cc < col; cc++) {
            int l = row-1; int r = row-1;
            while (r >= 0) {
                while (r > 0 && board[r][cc] < 0) {
                    board[r][cc] = 0;
                    r--;
                }
                
                while (l > r && board[l][cc] > 0) {
                    l--;
                }
                if (board[l][cc] <= 0 && board[r][cc] >= 0) {
                    board[l][cc] = board[r][cc];
                    board[r][cc] = 0;
                }
                l--; r--;
                
            }
            //System.out.println(l);
            if (board[0][cc] < 0) {
                board[0][cc] = 0;
            }
            
            
        }
    }
    
    public boolean candyMatchCol(int[][] board) {
        int row = board.length; int col = board[0].length;
        boolean isStable = true;
        for (int cc = 0; cc < col; cc++) {
            int l = 0; int r = 0;
            while (r < row) {
                if (board[r][cc] == 0) {
                    r++; l=r;
                    continue;
                }
                while (r < row  && Math.abs(board[l][cc]) == Math.abs(board[r][cc])) {
                    r++;
                }
                
                if (r-l+1 > 3) {
                    isStable = false;
                    while (l < r) {
                        if (board[l][cc] > 0) board[l][cc] *= -1;
                        l++;
                    }
                }
                l = r;
                
            }
        }
        
        return isStable;
        
    }
    
    public boolean candyMatchRow(int[][] board) {
        int row = board.length; int col = board[0].length;
        
        //row
        boolean isStable = true;
        for (int cr = 0; cr < row; cr++) {
            int l = 0; int r = 0;
            
            while (r < col) {
                if (board[cr][r] == 0) {
                    r++; l = r;
                    continue;
                }
                while (r < col && Math.abs(board[cr][l]) == Math.abs(board[cr][r])) {
                    r++;
                }
                if ((r-l+1) > 3) {
                    isStable = false;
                    while (l < r) {
                        if (board[cr][l] > 0) board[cr][l] *= -1;
                        l++;
                    }
                }
                l = r;
            }
            
        }
        return isStable;
    }
}