class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        # nC = 3, prereq = [[1,0],[1,2],[0,1]]
        
        graph = collections.defaultdict(set)
        for cl, prereq in prerequisites:
            inDegree[cl] += 1
            graph[prereq].add(cl)
        #print(inDegree, graph)  
        """
            0 -> 1
            2 -> 1
        """
        q = collections.deque()
        for cl, prereqCount in enumerate(inDegree):
            if prereqCount == 0:
                q.append(cl)
        
        res = []
        while q:
            prereq = q.popleft()
            res.append(prereq)
            
            for nxtClass in graph[prereq]:
                inDegree[nxtClass] -= 1
                if inDegree[nxtClass] == 0: q.append(nxtClass)
        return res if len(res) == numCourses else []