class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #detect loops
        #if anytime reach a dead end, return False

        if source == destination: 
            if not edges: return True
            else: return False
        
        graphRep = collections.defaultdict(set)
        #create graphRep
        for e1, e2 in edges:
            graphRep[e1].add(e2)

 
        def dfs(visited, currVisit, parent):

            if currVisit in visited: return False
            if currVisit != destination and len(graphRep[currVisit]) == 0: return False
            
            visited.add(currVisit)
            for choice in graphRep[currVisit]:
                
                ans = dfs(visited, choice, currVisit)
                if not ans:
                    return False
            visited.remove(currVisit)
            return True  
        
        a = dfs(set(), source, source)
        return a