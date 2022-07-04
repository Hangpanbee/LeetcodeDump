class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        
        for i in range(m-1):
            
            #backward
            for j in range(n-2, -1, -1):
                prevVal = points[i][j+1]-1 if j+1 < n else 0
                points[i][j] = max(prevVal, points[i][j])
                
            #forward
            for j in range(n):
                prevVal = points[i][j-1]-1 if j else 0
                points[i][j] = max(prevVal, points[i][j])
                points[i+1][j] += points[i][j]
                       
        return max(points[-1])
        