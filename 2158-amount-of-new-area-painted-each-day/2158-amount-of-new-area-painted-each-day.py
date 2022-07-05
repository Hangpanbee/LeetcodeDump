class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        START = 1
        END = -1
        paints = []
        for i, (s, e) in enumerate(paint):
            paints.append((s, START, i))
            paints.append((e, END, i))
        
        paints.sort()
        active = []
        ans = [0]*len(paint)
        prevp = 0
        for p in paints:
            pa, STATUS, i = p
            if active:
                ans[active[0]] += pa - prevp
            if STATUS == END:
                while active and pa >= paint[active[0]][1]:
                    heapq.heappop(active)
            elif STATUS == START:
                heapq.heappush(active, i)
            prevp = pa

        return ans