class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        lastEnd = -1
        for start, end in intervals:
            if lastEnd > start:
                return False
            lastEnd = end
        
        return True
        