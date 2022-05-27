class TimeMap:

    def __init__(self):
        self.TimeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        runtime: o(1)
        """
        if key not in self.TimeMap:
            self.TimeMap[key].append(("",0))
        self.TimeMap[key].append( (value, timestamp))
        # -> {foo: (bar, 1)}

    def get(self, key: str, timestamp: int) -> str:
        """
        runtime: o(logN * g)
        """
        if key not in self.TimeMap: return ""
        getTS = lambda x: x[1]
        getKeyPos = self.binarySearch(self.TimeMap[key], timestamp, getTS)
        return self.TimeMap[key][getKeyPos][0]
        
    def binarySearch(self, a, target, key=lambda x: x):
        l, r = 0, len(a)-1
        # [1,4] ->  target = 1 -> mid = 0 -> l = mid 
        # [1,4] -> l, r = 0, 1 -> mid = 
        while l < r:
            mid = l + (r-l+1)//2
            if key(a[mid]) <= target:
                l = mid
            elif key(a[mid]) > target:
                r = mid - 1
                
        return l

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)