class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_guest = 0
        map = defaultdict(list)
        for i in range(len(trips)):
            map[trips[i][1]].append(["p", trips[i][0]])
            map[trips[i][2]].append(["d", trips[i][0]])
        map_sorted = sorted(map.items(), key = lambda x: x[0])
        for k, v in map_sorted:
            for i in range(len(v)):
                #print(v[i][1])
                if v[i][0] == "p": curr_guest += v[i][1]
                if v[i][0] == "d": curr_guest -= v[i][1]
            
            if curr_guest > capacity: return False
        return True
        
        