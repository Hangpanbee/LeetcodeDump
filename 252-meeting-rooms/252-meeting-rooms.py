class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        lastEnd = -1
        for interval in intervals:
            if lastEnd > interval[0]:
                return False
            else:
                lastEnd = interval[1]
        
        return True
        