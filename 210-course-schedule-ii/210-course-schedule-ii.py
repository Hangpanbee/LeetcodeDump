class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        self.graph = collections.defaultdict(set)
  
        for cl, prereq in prerequisites:
            self.graph[cl].add(prereq)
        #print(inDegree, graph)  
       
        self.visited = {}
        self.courses = []
        for cl in range(numCourses):
            isValid = self.dfs(cl)
            if not isValid: return []
            
        return self.courses
            
            
    def dfs(self, currCourse):
        
        if currCourse in self.visited:
            return self.visited[currCourse]
        self.visited[currCourse] = False
        
        for nxtClass in self.graph[currCourse]:
            isNotCyclic = self.dfs(nxtClass)
            if not isNotCyclic: return False
        
        self.courses.append(currCourse)
        self.visited[currCourse] = True
        
        return True