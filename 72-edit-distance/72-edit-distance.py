class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: return len(word2)
        elif not word2: return len(word1)
        """
        w1 = "horse" w2 = "ros"
        -> i1, i2 = 0, 0
            -> replace r -> rorse
            -> insert rhorse
            -> orse 
        -> i1, i2 = 1, 1
            -> replace 
            -> 
            
        w1 = "ros" w2 = "horse"
        
        """
        memoize = {}
        def dp(i1, i2):
            
            if (i1 == len(word1)): return len(word2) - i2
            elif (i1, i2) in memoize: return memoize[(i1, i2)]
            
            replace, insert, delete = float(inf), float(inf), float(inf)
            if i2 < len(word2):
                if (word1[i1] != word2[i2]): 
                    replace = 1 + dp(i1+1, i2+1)
                else:
                    replace = dp(i1+1, i2+1)
                insert = 1 + dp(i1, i2+1)
                delete = 1 + dp(i1+1, i2)
            else:
                delete = 1 + dp(i1+1, i2)
            memoize[(i1, i2)] = min(replace, insert, delete)
            
            return memoize[(i1, i2)]
        
        
        return dp(0, 0)