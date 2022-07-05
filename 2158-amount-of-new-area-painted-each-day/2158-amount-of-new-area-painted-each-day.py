class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        START = 1
        END = -1
        maxPaint = 0
        minPaint = float(inf)
        paints = []
        for i, (s, e) in enumerate(paint):
            paints.append((s, START, i))
            paints.append((e, END, i))
            maxPaint = max(maxPaint, e)
            minPaint = min(minPaint, s)
        
        paints.sort()
        """
        paints = [(4,1,2),(11,1,0),(13,1,1),(14,-1,1),(18,-1,0),(20,-1,2)]
        """
        pi = 0
        active = []
        ans = [0]*len(paint)
        for p in range(minPaint, maxPaint+1):
            if active:
                ans[active[0]] += 1
            """
            ans = [7,0,7]
            p = 4
            p = 11
            p = 13
            p = 14
            p = 18
            """
            while pi < len(paints) and paints[pi][0] == p:
                pa, STATUS, i = paints[pi]

                if STATUS == END:
                    while active and p >= paint[active[0]][1]:
                        heapq.heappop(active)
                elif STATUS == START:
                    heapq.heappush(active, i)
                    # active = [0,1,2]
                pi += 1
                
        return ans