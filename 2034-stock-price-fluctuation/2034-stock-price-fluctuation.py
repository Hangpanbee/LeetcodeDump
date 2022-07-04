class StockPrice:

    def __init__(self):
        self.streamingMin = []
        self.streamingMax = []
        self.stock = {}
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.streamingMin, (price, timestamp))
        heapq.heappush(self.streamingMax, (-price, timestamp))
        self.stock[timestamp] = price
        self.latest = max(self.latest, timestamp)
    
    

    def current(self) -> int:
        return self.stock[self.latest]
        
    def maximum(self) -> int:
        currMaxPrice, currTS = self.streamingMax[0]
        #print(self.stock, currTS, self.streamingMax)
        while self.stock[currTS] != -currMaxPrice:
            heapq.heappop(self.streamingMax)
            currMaxPrice, currTS = self.streamingMax[0]
        return currMaxPrice*(-1)
        

    def minimum(self) -> int:
        currMinPrice, currTS = self.streamingMin[0]
        while self.stock[currTS] != currMinPrice:
            heapq.heappop(self.streamingMin)
            currMinPrice, currTS = self.streamingMin[0]
        return currMinPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()