
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k_course: int) -> int:
        indegree = {}
        outdegree_map = collections.defaultdict(list)
        
        for i in range(1, n+1):
            indegree[i] = 0
        
        
        for prevCourse, nextCourse in relations:
            outdegree_map[prevCourse].append(nextCourse)
            indegree[nextCourse] = indegree[nextCourse] + 1

            
        @lru_cache(None)
        def dp(indegree_1):
            
            course_can_take = []
            indegree_1 = dict(indegree_1)
            for k, v in indegree_1.items():
                if v == 0:
                    course_can_take.append(k)
            
            #print(course_can_take)
            if len(course_can_take) == 0:
                return 0

            ans = float(inf)
            
            for choice in itertools.combinations(course_can_take, min(len(course_can_take),k_course) ):
                indegree = indegree_1.copy()
                for course in choice:
                    indegree[course] -= 1
                    for nextCourse in outdegree_map[course]:
                        indegree[nextCourse] -= 1

                ans = min(ans, 1 + dp(tuple(indegree.items())))
                
            return ans
        
        return dp(tuple(indegree.items()))

                        
             
        
        
        
        