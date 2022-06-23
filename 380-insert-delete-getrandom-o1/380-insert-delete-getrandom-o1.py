from random import choice

class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.valArr = []
        self.currIndex = 0

    def insert(self, val: int) -> bool:
        if val in self.seen: return False
        else: 
            self.seen[val] = len(self.valArr)
            self.valArr.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        can delete by swapping the value to the tail
        """
        if val in self.seen:
            valIndex = self.seen[val]
            lastEle = self.valArr[-1]
            self.seen[lastEle] = valIndex
            self.valArr[valIndex], self.valArr[-1] = lastEle, self.valArr[valIndex]
            
            del self.seen[val]
            self.valArr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        #rand = random.randrange(0, len(self.valArr))
        
        return choice(self.valArr)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()