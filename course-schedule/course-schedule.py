class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not len(prerequisites): return True
        
        graphRep = collections.defaultdict(set)
        edgeCount = [-1] * numCourses
        numAvailCourseSet = set()
        
        for con1, con2 in prerequisites:
            numAvailCourseSet.add(con1)
            numAvailCourseSet.add(con2)
            graphRep[con2].add(con1)
            if edgeCount[con1] == -1: edgeCount[con1] = 1
            elif edgeCount[con1] != -1: edgeCount[con1] += 1
            
            if edgeCount[con2] == -1: edgeCount[con2] = 0

        
        numAvailCourses = len(numAvailCourseSet)
        
        dq = collections.deque()
        for loneNode in range(len(edgeCount)):
            if edgeCount[loneNode] == 0:
                dq.append(loneNode)
            


        nodeVisitedCount = 0
        while dq:
            loneNode = dq.popleft()
            nodeVisitedCount += 1
            if nodeVisitedCount > numAvailCourses: break
            
            for outNode in graphRep[loneNode]:
                edgeCount[outNode] -= 1
                if edgeCount[outNode] == 0:
                    dq.append(outNode)
        
        #print(nodeVisitedCount, numAvailCourses)
        return False if nodeVisitedCount != numAvailCourses else True
            
            
        
        
            
        