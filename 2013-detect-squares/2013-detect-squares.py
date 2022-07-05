class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] += 1

    def count(self, point: List[int]) -> int:
        x2, y2 = point
        ans = 0
        #print(self.points)
        for (x1, y1), v in self.points.items():
            if abs(x2-x1) != abs(y2-y1): continue
            if x1 != x2 and y1 != y2 and (x1,y2) in self.points and (x2, y1) in self.points:
                ans += v*self.points[(x1, y2)]*self.points[(x2,y1)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)