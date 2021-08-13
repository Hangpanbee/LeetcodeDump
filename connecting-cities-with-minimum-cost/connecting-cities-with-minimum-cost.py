class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n-1): return -1
        
        graph = collections.defaultdict(set)
        
        #preprocessing
        for city1, city2, cost in connections:
            graph[city1].add((cost, city2))
            graph[city2].add((cost, city1))
        
        
        #pick a random vertice to start
        pq = list(graph[1])
        visited = {1}
        costSum = 0
        
        heapq.heapify(pq)
        
        while len(pq) != 0:
            cost, currCity = heapq.heappop(pq)
            
            if currCity not in visited:
                visited.add(currCity)
                costSum += cost
                
                for nextCost, nextCity in graph[currCity]:
                    heapq.heappush(pq, (nextCost, nextCity))
                    
        return costSum if len(visited) == n else -1
        
        
        
        