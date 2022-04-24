class UndergroundSystem:

    def __init__(self):
        self.customerCheckIn = collections.defaultdict(tuple)
        self.train = collections.defaultdict(tuple)
    

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerCheckIn[id] = (stationName, t)

    def checkOut(self, id: int, checkOutStation: str, t: int) -> None:
        checkInStation, checkInTime = self.customerCheckIn[id]
        del self.customerCheckIn[id]
        
        if (checkInStation, checkOutStation) not in self.train:
            self.train[(checkInStation, checkOutStation)] = (t-checkInTime ,1)
            return
        
        prevAvgTime, prevCount = self.train[(checkInStation, checkOutStation)]
        self.train[(checkInStation, checkOutStation)] = ( (prevAvgTime*(prevCount)+(t-checkInTime))/(prevCount+1), prevCount+1)
        return
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.train[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)