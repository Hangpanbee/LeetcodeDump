class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        n1, n2 = 0, 0
        heapq.heappush(heap, [nums1[n1]+nums2[n2], n1, n2])
        ans = []
        tracker = {}
        while len(ans) < k and heap:
            curr_choice, n1, n2 = heapq.heappop(heap)
            ans.append([nums1[n1], nums2[n2]])
           
            if n1+1 < len(nums1) and (n1+1, n2) not in tracker:
                left_choice = nums1[n1+1] + nums2[n2]
                heapq.heappush(heap, [left_choice, n1+1, n2])
                tracker[(n1+1, n2)] = True
            if n2+1 < len(nums2) and (n1, n2+1) not in tracker:
                down_choice = nums2[n2+1] + nums1[n1]
                heapq.heappush(heap, [down_choice, n1, n2+1])
                tracker[(n1, n2+1)] = True
                

        return ans
        