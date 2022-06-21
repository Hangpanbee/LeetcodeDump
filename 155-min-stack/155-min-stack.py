class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, val))
        else:
            self.minStack.append((val, min(val, self.minStack[-1][1])))

    def pop(self) -> None:
        return self.minStack.pop()[0]

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()