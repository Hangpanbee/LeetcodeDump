"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        allSchedules = []
        for employee in schedule:
            for timeSlot in employee:
                allSchedules.append((timeSlot.start, timeSlot.end))
                
        
        heapq.heapify(allSchedules)
        fstVal = Interval()
        fstVal.start, fstVal.end = float(-inf), 0
        currFreee = [fstVal]


        
        while len(allSchedules) != 0:
            compareStart, compareEnd = heapq.heappop(allSchedules)

            if compareStart > currFreee[-1].start:
                currFreee[-1].end = compareStart
                newInterval = Interval()
                newInterval.start = compareEnd
                newInterval.end = float(inf)
                currFreee.append(newInterval)
            else:
                currFreee[-2].end = min(currFreee[-2].end, compareStart)
                currFreee[-1].start = max(currFreee[-1].start, compareEnd)
            #todo think about equal case (1,3) (3,4)
        
        currFreee.pop(0)
        currFreee.pop()

        return currFreee
        
    
        