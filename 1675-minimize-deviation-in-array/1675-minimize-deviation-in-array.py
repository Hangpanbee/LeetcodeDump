class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_heap = []

        for i, num in enumerate(nums):
            if num%2==1:
                nums[i] = num*2
            heapq.heappush(heap, -nums[i])
            heapq.heappush(min_heap, nums[i])
   
        #use priority queue instead
        min_diff = 9999999999
        while heap[0]%2==0:
            max_num = heapq.heappop(heap)//2
            if -max_num < min_heap[0]:
                heapq.heappush(min_heap, -max_num)
            heapq.heappush(heap, max_num)
            min_diff = min(min_diff, -heap[0] - min_heap[0])
       
        return min_diff