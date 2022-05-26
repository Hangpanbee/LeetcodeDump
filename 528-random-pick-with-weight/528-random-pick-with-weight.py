class Solution:

    def __init__(self, w: List[int]):
        self.w = [0]
        runningSum = 0
        for i, v in enumerate(w):
            runningSum += v
            self.w.append(runningSum)
        self.sumW = runningSum
        

    def pickIndex(self) -> int:
        if self.sumW == 1: return 0
        currP = random.randint(1,self.w[-1])
        #print(currP, self.sumW, self.w)
        currI = bisect.bisect_left(self.w, currP)
        #print(currI)
        return currI - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()