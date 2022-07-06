class RangeModule:
    """
        [9,93]
    """
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        li = bisect.bisect_left(self.intervals, left)
        ri = bisect.bisect_right(self.intervals, right)
        
        newRange = []
        if li%2 == 0:
            newRange.append(left)
        if ri%2 == 0:
            newRange.append(right)
            
        self.intervals[li:ri] = newRange

    def queryRange(self, left: int, right: int) -> bool:
        li = bisect.bisect_right(self.intervals, left)
        ri = bisect.bisect_left(self.intervals, right)
        #print(self.intervals)
        return (li%2==1 and ri%2==1 and li == ri)

    def removeRange(self, left: int, right: int) -> None:
        
        li = bisect.bisect_right(self.intervals, left)
        ri = bisect.bisect_left(self.intervals, right)
        
        newRange = []
        if li%2 == 1:
            newRange.append(left)
        if ri%2 == 1:
            newRange.append(right)
            
        self.intervals[li:ri] = newRange


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)