class MyHashMap:

    def __init__(self):
        self.HashMap = {}

    def put(self, key: int, value: int) -> None:
        self.HashMap[key] = value

    def get(self, key: int) -> int:
        return self.HashMap[key] if key in self.HashMap else -1

    def remove(self, key: int) -> None:
        if key in self.HashMap:
            del self.HashMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)