class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        

        def dfs(r, c, i, seen):
            if i == len(word): return True
            
            for dr, dc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= dr < m and 0 <= dc < n and board[dr][dc] == word[i] and (dr, dc) not in seen:
                    seen.add((dr, dc))
                    isWord = dfs(dr, dc, i+1, seen)
                    if isWord: return True
                    seen.remove((dr, dc))
                    
            return False
        
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    seen = set()
                    seen.add((r, c))
                    if dfs(r, c, 1, seen): return True
        return False
        
        