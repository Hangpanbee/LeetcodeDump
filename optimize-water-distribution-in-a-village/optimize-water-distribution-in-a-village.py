class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        Well = [(cost, house + 1) for house, cost in enumerate(wells)]
        
        graphH1H2 = collections.defaultdict(set)
        #preprocessing
        for h1, h2, cost in pipes:
            graphH1H2[h1].add((cost, h2))
            graphH1H2[h2].add((cost, h1))
        
        connectedHouse = [False] * (n+1)
        houseCount, costSum = 0, 0
        heapq.heapify(Well)
        
        while houseCount < n:
            cost, currHouse = heapq.heappop(Well)
            
            if connectedHouse[currHouse] == False:
                houseCount += 1
                costSum += cost
                connectedHouse[currHouse] = True
                
                #logic to connect as many house as possible
                #or should i?
                for cost, house in graphH1H2[currHouse]:
                    heapq.heappush(Well, (cost, house))
               
                    
            else:
                continue
            
            
        return costSum
        