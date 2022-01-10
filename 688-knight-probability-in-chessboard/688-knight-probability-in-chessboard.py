class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.moves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        self.memoize = {}
        self.onBoard = 0

        @lru_cache(None)
        def backtrack(n, k, curr_row, curr_col, curr_move):
            if curr_move == k:
                return 1
                
            if (curr_row, curr_col, curr_move) in self.memoize:
                return self.memoize[(curr_row, curr_col, curr_move)]
            
            self.memoize[(curr_row, curr_col, curr_move)] = 0
            
            for choice in self.moves:
                row_choice, col_choice = choice[0], choice[1]
                new_row = curr_row + row_choice
                new_col = curr_col + col_choice
                if new_row >= n or new_col >= n or new_row < 0 or new_col < 0:
                    continue

                self.memoize[(curr_row, curr_col, curr_move)] += backtrack(n, k, new_row, new_col, curr_move + 1)
                
            return self.memoize[(curr_row, curr_col, curr_move)]
        
        return backtrack(n, k, row, column, 0)/8**k
