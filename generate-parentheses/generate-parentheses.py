class Solution:
    def __init__(self):
        self.ans_list = []
    
    def generateParenthesis(self, n: int) -> List[str]:
       
        def recurParen(l, r, paren):
            if l < r or l > n or r > n: return
            if len(paren) == n*2 and l == r == n: 
                self.ans_list.append(paren)
                return
            
            #there are 2 choices at any given moment
            recurParen(l+1,r,paren+"(")
            recurParen(l,r+1,paren+")")
            
        recurParen(0,0,"")
        return self.ans_list