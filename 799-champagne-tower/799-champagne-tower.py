class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [0]*101
        res[0] = poured
        
        for row in range(1, query_row+1):
            for i in range(row, -1, -1):
                res[i] = max(0, (res[i]-1)/2)
                res[i+1] += res[i]
                
        return min(1.0, res[query_glass]) 
        