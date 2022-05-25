class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], T: int, target: int) -> float:
        
        graph = collections.defaultdict(set)
        for e1, e2 in edges:
            graph[e1].add(e2)
            graph[e2].add(e1)
            
        def dfs(vert, t, visited):
            
            if t == T and vert == target:
                return 1
            elif t == T:
                return 0
            elif vert == target:
                #print(vert, t)
                isStuck = False
                for way in graph[vert]:
                    isStuck = isStuck or not visited[way]
                return 1 if not isStuck else 0
         
            totalChance = 0
            chance = 0
            for nxtVertex in graph[vert]:
                if visited[nxtVertex]: continue
                chance += 1
            
            for nxtVertex in graph[vert]:
                if visited[nxtVertex]: continue
                visited[nxtVertex] = True
                totalChance += 1/chance*dfs(nxtVertex, t+1, visited)
                visited[nxtVertex] = False
      
            return totalChance
        
        visited = [False]*(n+1)
        visited[1] = True
        a = dfs(1, 0, visited)
     
        return a
        
        