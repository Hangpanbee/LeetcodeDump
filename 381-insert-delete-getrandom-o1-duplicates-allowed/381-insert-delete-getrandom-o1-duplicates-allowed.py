from random import choice
class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.dict = collections.defaultdict(list)

    def insert(self, val: int) -> bool:

        self.dict[val].append(len(self.arr))
        self.arr.append(val)
        if len(self.dict[val]) > 1:
            return False
        else:
            return True
        # self.arr = [4,3,4,2,4]
        # self.dict = {4:[0,2,4], 3:[1], 2: [3]}

    def remove(self, val: int) -> bool:
        # val = 4 -> self.arr = [4,3,4,2], self.dict={4:[0,2],3:[1],2:[3]}
        # val = 3 -> self.arr = []
        #print(self.dict, val)
        if val in self.dict:    
            valI = self.dict[val].pop()
            if not self.dict[val]: del self.dict[val]
            if valI == len(self.arr)-1:
                self.arr.pop()
                return True
            lastEle = self.arr[-1]
            if self.dict[lastEle]: 
                self.dict[lastEle].pop()
                if not self.dict[lastEle]: del self.dict[lastEle]
            self.dict[lastEle].append(valI)
            self.dict[lastEle].sort()
            #print(valI, self.arr)
            self.arr[valI], self.arr[-1] = self.arr[-1], self.arr[valI]
            self.arr.pop()
            
            return True
        else:
            return False
        
        

    def getRandom(self) -> int:
        
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()