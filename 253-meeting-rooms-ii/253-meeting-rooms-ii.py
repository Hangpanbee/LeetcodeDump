class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        endingHeap = []
        
        
        for s, e in intervals:
            heapq.heappush(endingHeap, e)
            if endingHeap[0] <= s: heapq.heappop(endingHeap)
                
        return len(endingHeap)