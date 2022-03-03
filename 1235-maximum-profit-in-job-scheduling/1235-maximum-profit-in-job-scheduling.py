class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        i = 0
        grouped_time = []
        while i < len(startTime):
            grouped_time.append([startTime[i], endTime[i], profit[i]])
            i += 1
        grouped_time.sort()        
        #print(grouped_time)
        pos = sorted(set(startTime + endTime))
        heap = []
        curr_job = 0
        curr_max = 0
        ans = 0
        for vs in pos:
            #print(heap)
            while heap and heap[0][0] == vs:
                end, value = heapq.heappop(heap)
                ans = max(-value, ans)
                curr_max = max(ans, -value)
            #print(curr_max, vs)
            while curr_job < len(startTime) and grouped_time[curr_job][0] == vs:
                heapq.heappush(heap, (grouped_time[curr_job][1], -(curr_max + grouped_time[curr_job][2])))
                curr_job += 1
            
            
            
        return ans
        
        
        