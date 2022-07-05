class SummaryRanges:

    def __init__(self):
        self.intervals = []        

    def addNum(self, val: int) -> None:
        vali = bisect.bisect_left(self.intervals, val)

        if vali%2 == 1: pass
        else:
            #if val == 60: 
                #print(self.intervals[26], val, vali)
            if vali+1 < len(self.intervals) and vali-1 >= 0 and self.intervals[vali] == val+1 and self.intervals[vali-1] == val-1:
                #print(self.intervals, val)
                self.intervals[vali-2:vali+2] = [self.intervals[vali-2], self.intervals[vali+1]]
            elif vali+1 < len(self.intervals) and self.intervals[vali] == val+1:
                self.intervals[vali] = val
            elif vali-1 >= 0 and self.intervals[vali-1] == val-1:
                self.intervals[vali-1] = val
            elif vali+1 < len(self.intervals) and self.intervals[vali] == val:
                pass
            elif vali-1 >= 0 and self.intervals[vali-1] == val:
                pass
            else:
                bisect.insort_left(self.intervals, val)
                bisect.insort_right(self.intervals, val)
        

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for i in range(0, len(self.intervals),2):
            intervals.append([self.intervals[i], self.intervals[i+1]]) 
        return intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()