class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap, ans = [], [[-1, -1]]
        building_pos = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
        curr_index = 0
        #print(building_pos)
        for line_pos in building_pos:
            
            while curr_index < len(buildings) and buildings[curr_index][0] == line_pos:
                heapq.heappush(heap, (-buildings[curr_index][2], buildings[curr_index][1]))
                curr_index += 1
            
            while heap and heap[0][1] <= line_pos:
                heapq.heappop(heap)
            
            if not heap: heapq.heappush(heap, (0, line_pos))
            if heap and -heap[0][0] != ans[-1][1]: 
                ans.append([line_pos, -heap[0][0]])
         
   
                
                
            
        return ans[1:]
            
            
        