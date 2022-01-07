
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.ans = []
        def backtrack(s, curr_pali):

            if len(s) == 0:
                self.ans.append(curr_pali)
            
            for i in range(1, len(s)+1):
                curr_chopped, next_s = s[:i], s[i:len(s)]
                if self.isPali(curr_chopped):
                    backtrack(next_s, curr_pali+[curr_chopped])
            return None
        
        backtrack(s, []) 
        return self.ans
        
        
        
    def isPali(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            else: 
                l += 1
                r -= 1
        return True
                
        