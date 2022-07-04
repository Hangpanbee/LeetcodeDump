class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        points_set = set([tuple(point) for point in points])
        smallest = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i:], i):
                if x1 < x2 and y1 < y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    area = (x2 - x1) * (y2 - y1)
                    smallest = min(smallest, area)
        return smallest if smallest != float('inf') else 0