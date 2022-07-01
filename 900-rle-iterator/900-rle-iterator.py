class RLEIterator:

    def __init__(self, encoding: List[int]):
        """
        [(3,8),(5,5),(6,8)]
        """
        runningSum = 0
        self.encoding = []
        for i in range(0, len(encoding), 2):
            if encoding[i] == 0: continue
            runningSum += encoding[i]
            self.encoding.append((runningSum, encoding[i+1]))
        self.iterator = 0
        self.lBoundary = 0

    def next(self, n: int) -> int:
        self.iterator += n
        # self.i = 4
        targetI = self.__binarySearch(self.iterator, self.lBoundary)
        self.lBoundary = targetI
        if targetI >= len(self.encoding):
            return -1
        else: return self.encoding[targetI][1]
    
    def __binarySearch(self, target, l) -> int:
        r = len(self.encoding)
        
        while l < r:
            mid = l + (r-l)//2
            
            if self.encoding[mid][0] < target:
                l = mid + 1
            else:
                r = mid
                
        return l


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)