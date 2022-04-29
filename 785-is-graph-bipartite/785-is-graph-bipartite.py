
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parent = [-1]*len(graph)
        A = 0
        B = 1
        q = collections.deque()   
        q.append(0)
        visited = {}
        
        while q:
            i = q.popleft()
            visited[i] = True
            iParent = parent[i]
            neighborGroup = B
            if iParent == -1 or iParent == A: 
                parent[i] = A
            else:
                neighborGroup = A

            for node in graph[i]:
                if node not in visited: q.append(node)
                if parent[node] == -1:
                    parent[node] = neighborGroup
                elif parent[node] == parent[i]: 
                   
                    return False
            if not q and len(visited) < len(graph):
                for iterator in range(len(graph)):
                    if iterator in visited: continue
                    else: q.append(iterator)
        
        return True
                