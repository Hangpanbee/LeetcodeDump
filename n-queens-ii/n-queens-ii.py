class Solution:
    
    def totalNQueens(self, row: int) -> List[List[str]]:
        """
        avoid: is a dictionary keep track of all of the position queen has been placed
        """
        ## primitive type cant be global varaible outside of the nested scope
        def dfs(avoid, n):
            if n == row: 
                return 1
            ## create a set of element to avoid
            avoidset = set()
            for key, val in avoid.items():
                avoidset.add(val)
                if val+n-key < row: avoidset.add(val+n-key)
                if val-n+key > -1: avoidset.add(val-(n-key))
            if len(avoidset) == row: return 0
            
            ## why put solution here?
            solution = 0
            for place in range(row):
                if place in avoidset: continue
                avoid[n] = place
                solution += dfs(avoid.copy(), n+1)
            return solution
        
        return dfs({}, 0)
        