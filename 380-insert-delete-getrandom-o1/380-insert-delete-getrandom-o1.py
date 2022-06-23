import random

class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.indexToVal = {}
        self.currIndex = 0

    def insert(self, val: int) -> bool:
        if val in self.seen: return False
        else: 
            self.seen[val] = self.currIndex
            self.indexToVal[self.currIndex] = val
            self.currIndex+=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.seen:
            valIndex = self.seen[val]
            del self.seen[val]
            del self.indexToVal[valIndex]
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand = random.randrange(0, self.currIndex)
        
        while (rand not in self.indexToVal):
            rand = random.randrange(0, self.currIndex)
        
        return self.indexToVal[rand]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()