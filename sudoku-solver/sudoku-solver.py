class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #what is the time complexity?
        
        #find valid choices
        unavailRowChoices = collections.defaultdict(set)
        unavailColChoices = collections.defaultdict(set)
        unavailBlockChoices = collections.defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    unavailRowChoices[row].add(board[row][col])
                    unavailColChoices[col].add(board[row][col])
                    unavailBlockChoices[col//3+row//3*3].add(board[row][col])
        #print(unavailBlockChoices)
        
        def helper(board, row, col):  
            #explore the current option
            #if we successfully reach the end: isValid(board[lastRow][lastCol]): return board     
            if col == 9 and row != 9: 
                row += 1
                col = 0
            if row == 9 and col == 0: return True
            
            # where to put this line?

            if board[row][col] != ".": return helper(board, row, col+1)

            #if the choices are impossible, then return to backtrack
            ## have to initiazlie invalid choices first or else it will be passed like a pointer
            invalidChoices = set()
            invalidChoices = unavailRowChoices[row].union(unavailColChoices[col])
            invalidChoices = invalidChoices.union(unavailBlockChoices[col//3+row//3*3])
            
            if len(invalidChoices) == 9: return False
            # for a b c d in valid choices
            for choice in range(1, 10):
                if str(choice) in invalidChoices: continue
                #print(row, col, invalidChoices)
                #chose
                board[row][col] = str(choice)
                unavailRowChoices[row].add(str(choice))
                unavailColChoices[col].add(str(choice))
                unavailBlockChoices[col//3+row//3*3].add(str(choice))
                #explore
                #if we found the solution: then escape
                #this is the last recursive call
                if helper(board.copy(), row, col+1): return True
                #unchoose
                board[row][col] = "."
                unavailRowChoices[row].remove(str(choice))
                unavailColChoices[col].remove(str(choice))
                unavailBlockChoices[col//3+row//3*3].remove(str(choice))
            return False    
        return helper(board, 0, 0)
        