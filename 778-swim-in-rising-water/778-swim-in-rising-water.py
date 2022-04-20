class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0]
        startHeap = []
        endHeap = []
        sVisited = {(0,0): 0}
        eVisited = {(n-1, n-1): 0}
        heapq.heappush(startHeap, (grid[0][0], 0, 0))
        heapq.heappush(endHeap, (grid[n-1][n-1], n-1, n-1))
        
        
        while startHeap and endHeap:
            sVal, sR, sC = heapq.heappop(startHeap)
            sVisited[(sR, sC)] = sVal
            for newSR, newSC in [(sR+1, sC), (sR-1, sC), (sR, sC+1), (sR, sC-1)]:
                
                if 0 <= newSR < n and 0 <= newSC < n and (newSR, newSC) not in sVisited:

                    if (newSR, newSC) in eVisited: 
                        #print(eVisited, "eVisited")
                        #print(sVisited)
                        return max(sVal, eVisited[(newSR, newSC)])
                    heapq.heappush(startHeap, (max(grid[newSR][newSC], sVal), newSR, newSC))
            
            eVal, eR, eC = heapq.heappop(endHeap)
            #print(eVisited)
            eVisited[(eR, eC)] = eVal
            for newER, newEC in [(eR+1, eC), (eR-1, eC), (eR, eC+1), (eR, eC-1)]:
                
                if 0 <= newER < n and 0 <= newEC < n and (newER, newEC) not in eVisited:
                    
                    if (newER, newEC) in sVisited: 
    
                        return max(sVisited[(newER, newEC)], eVal)
                    heapq.heappush(endHeap, (max(grid[newER][newEC], eVal), newER, newEC))
                    
                    
        
        
        #Bidirectional BFS
      
