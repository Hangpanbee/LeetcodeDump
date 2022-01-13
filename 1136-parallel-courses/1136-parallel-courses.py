class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        in_degree = [0]*(n+1)
        outdegree_map = collections.defaultdict(list)
        
        for prev, nextCourse in relations:
            outdegree_map[prev].append(nextCourse)
            in_degree[nextCourse] += 1
            
        #print(outdegree_map, in_degree)
        q = deque()
        for i, v in enumerate(in_degree):
            if v == 0 and i > 0:
                q.append((i, 1))

        min_sem = -1
        course_taken = 0
        while q:
            curr_class, curr_sem = q.popleft()
            course_taken += 1
            min_sem = max(curr_sem, min_sem)
            for i in outdegree_map[curr_class]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append((i, curr_sem+1))
        
        
        return min_sem if course_taken == n else -1
        