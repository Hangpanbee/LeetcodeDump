class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # ask if it is from 0 up to numcourse of is it 1th index?
        
        
        inEdge = [0]*numCourses
        #graph = collections.defaultdict(set)
        prereqGraph = collections.defaultdict(set)
        
        for course, prereq in prerequisites:
            #graph[course].add(prereq)
            prereqGraph[prereq].add(course)
            inEdge[course] += 1
        
        # prereq = [[1,0], [0, 1]]
        # prereq = []
        
        # -> [[1, 0], [2, 0], [3, 1], [3, 2]] numCourses = 4
        # -> inEdge = [0, 1, 1, 2]
        # -> prereqGraph = { 0 : [1, 2], 1: [3], 2: [3], 3: [] }
        q = collections.deque()
        coursesToTake = []
        for course, numPrereq in enumerate(inEdge):
            if numPrereq == 0:
                q.append(course)
                coursesToTake.append(course)
        # -> q = deque([0]) -> coursesToTake = [0]  
        
        while q:
            currCourse = q.popleft()
            # -> currCourse = 0
            # -> currCourse = 1
            # -> currCourse = 2
            for nxtCourse in prereqGraph[currCourse]:
                inEdge[nxtCourse] -= 1
                if inEdge[nxtCourse] == 0:
                    q.append(nxtCourse)
                    coursesToTake.append(nxtCourse)
            # -> prereqGraph[0] -> [1, 2] -> inEdge = [0, 0, 0,2] -> q = deque([1, 2]) -> coursesToTake = [0, 1, 2]
            # -> prereqGraph[1] -> [3] -> inEdge = [0,0,0, 1] -> q = deque([2]) -> coursesToTake = [0, 1, 2]
            # -> prereqGraph[2] -> [3] -> inEdge = [0, 0, 0, 0] -> q = deque([]) -> coursesToTake = [0, 1, 2, 3]
        
        
        return coursesToTake if len(coursesToTake) == numCourses else []