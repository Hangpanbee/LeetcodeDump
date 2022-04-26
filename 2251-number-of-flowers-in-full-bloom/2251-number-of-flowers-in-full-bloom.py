class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        timeLine = sorted(list(set([ i for s, e in flowers for i in (s, e)] + [i for i in persons])))
        
        flowers.sort()
        persons = [(v, i) for i, v in enumerate(persons)]
        persons.sort()
        activeHeap = []
        i = 0
        pI = 0
        ans = [0]*len(persons)

        for tl in timeLine:
            
            while i < len(flowers) and tl == flowers[i][0]:
                heapq.heappush(activeHeap, (flowers[i][1], flowers[i][0]))
                i+=1
                
            while pI < len(persons) and tl == persons[pI][0]:
                #print(activeHeap, pI, tl, len(activeHeap))
                time, index = persons[pI]
                #print(time, index)
                ans[index] = len(activeHeap)
                #print(ans)
                pI += 1
            #print(tl, activeHeap)   
            while activeHeap and tl == activeHeap[0][0]:
                heapq.heappop(activeHeap)
        
        
        
        return ans