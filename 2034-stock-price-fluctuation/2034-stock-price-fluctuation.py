class StockPrice:

    def __init__(self):
        self.streamingMin = []
        self.streamingMax = []
        self.stock = {}
        self.latest = []

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.streamingMin, (price, timestamp))
        heapq.heappush(self.streamingMax, (-price, timestamp))
        heapq.heappush(self.latest, -timestamp)
        self.stock[timestamp] = price
    
    

    def current(self) -> int:
        currTS = heapq.heappop(self.latest)
        heapq.heappush(self.latest, currTS)
        return self.stock[-currTS]
        
    def maximum(self) -> int:
        currMaxPrice, currTS = heapq.heappop(self.streamingMax)
        #print(self.stock, currTS, self.streamingMax)
        while self.stock[currTS] != -currMaxPrice:
            currMaxPrice, currTS = heapq.heappop(self.streamingMax)
        heapq.heappush(self.streamingMax, (currMaxPrice, currTS))
        return currMaxPrice*(-1)
        

    def minimum(self) -> int:
        currMinPrice, currTS = heapq.heappop(self.streamingMin)
        while self.stock[currTS] != currMinPrice:
            currMinPrice, currTS = heapq.heappop(self.streamingMin)
        heapq.heappush(self.streamingMin, (currMinPrice, currTS))
        return currMinPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()