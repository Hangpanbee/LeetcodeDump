class MyHashSet:

    def __init__(self):
        self.HashSet = {}

    def add(self, key: int) -> None:
        self.HashSet[key] = 1

    def remove(self, key: int) -> None:
        if key in self.HashSet: del self.HashSet[key]

    def contains(self, key: int) -> bool:
        return key in self.HashSet
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)