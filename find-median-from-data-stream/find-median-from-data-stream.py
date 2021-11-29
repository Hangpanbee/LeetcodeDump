class MedianFinder:

    def __init__(self):
        #min heap is the natural heap
        self.lower_heap = [] #maxheap
        self.higher_heap = [] #minheap
        

    def addNum(self, num: int) -> None:
        max_lower_heap = self.lower_heap[0]*(-1) if len(self.lower_heap) > 0 else 99999999
        min_higher_heap = self.higher_heap[0] if len(self.higher_heap) > 0 else 99999999
        #print(num, max_lower_heap, min_higher_heap, len(self.lower_heap), len(self.higher_heap))
        if len(self.lower_heap) == len(self.higher_heap):
            if num <= min_higher_heap:
                heapq.heappush(self.lower_heap, num*(-1))
            elif num > max_lower_heap:
                heapq.heappush(self.higher_heap, num)
        elif len(self.lower_heap) > len(self.higher_heap):
            if num >= max_lower_heap:
                heapq.heappush(self.higher_heap, num)
            elif num < min_higher_heap:
                max_lower_heap_pop = heapq.heappop(self.lower_heap)*(-1)
                heapq.heappush(self.lower_heap, num*(-1))
                heapq.heappush(self.higher_heap, max_lower_heap_pop)
        elif len(self.higher_heap) > len(self.lower_heap):
            if num < min_higher_heap:
                heapq.heappush(self.lower_heap, num*(-1))
            
            elif num > max_lower_heap:
                min_higher_heap_pop = heapq.heappop(self.higher_heap)
                heapq.heappush(self.higher_heap, num)
                heapq.heappush(self.lower_heap, min_higher_heap_pop*(-1))      
                
            
        

    def findMedian(self) -> float:
        if len(self.lower_heap) == len(self.higher_heap):
            max_lower_heap = self.lower_heap[0]*(-1)
            min_higher_heap = self.higher_heap[0]
            return (min_higher_heap + max_lower_heap)/2
        elif len(self.lower_heap) > len(self.higher_heap):
            return self.lower_heap[0]*(-1)
        else:
            return self.higher_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()