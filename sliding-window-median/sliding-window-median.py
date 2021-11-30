class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left_maxHeap = []
        right_minHeap = []
        left_dict = {}
        right_dict = {}
        self.left_len, self.right_len = 0, 0
        median_list = []
        
        
        for i in range(len(nums)):
            num = nums[i]
            max_left_heap = left_maxHeap[0]*(-1) if self.left_len > 0 else -9999999999
            min_right_heap = right_minHeap[0] if self.right_len > 0 else 9999999999
            
            #add first
            if self.left_len == self.right_len:
                if num <= min_right_heap:
                    self.left_len = self.add_to_heap(num*(-1), left_maxHeap, left_dict, self.left_len)
                elif num > max_left_heap:
                    self.right_len = self.add_to_heap(num, right_minHeap, right_dict, self.right_len)
            elif self.left_len > self.right_len:
                if num > max_left_heap:
                    self.right_len = self.add_to_heap(num, right_minHeap, right_dict, self.right_len)
                elif num <= min_right_heap:
                    self.left_len = self.add_to_heap(num*(-1), left_maxHeap, left_dict, self.left_len)
            elif self.left_len < self.right_len:
                if num <= min_right_heap:
                    self.left_len = self.add_to_heap(num*(-1), left_maxHeap, left_dict, self.left_len)
                elif num > max_left_heap:
                    self.right_len =self.add_to_heap(num, right_minHeap, right_dict, self.right_len)
            
            #print("checkpoint FIRST", self.left_len, self.right_len, left_dict, right_dict, i, "\n")  

            if i >= k:
                deleted_num = nums[i-k]
                if deleted_num < min_right_heap: #rmv from left heap
                    self.left_len = self.remove_frm_heap(deleted_num*(-1), left_dict, self.left_len)
                elif deleted_num >= max_left_heap:
                    self.right_len = self.remove_frm_heap(deleted_num, right_dict, self.right_len)
            
            #print("checkpoint SECOND", self.left_len, self.right_len, left_dict, right_dict, "\n")  
            
            while self.right_len > self.left_len:
                min_right_heap_pop = heapq.heappop(right_minHeap)
                if min_right_heap_pop in right_dict:
                    self.right_len = self.remove_frm_heap(min_right_heap_pop, right_dict, self.right_len)
                    self.left_len = self.add_to_heap(min_right_heap_pop*(-1), left_maxHeap, left_dict, self.left_len)
                else: continue
            
            #print("checkpoint THIRD", self.left_len, self.right_len, left_dict, right_dict, "\n \n") 
            while (self.left_len - 1) > self.right_len:
                #print(self.left_len, self.right_len)
                max_left_heap_pop = heapq.heappop(left_maxHeap)*(-1)
                if max_left_heap_pop*(-1) in left_dict:
                    self.left_len = self.remove_frm_heap(max_left_heap_pop*(-1), left_dict, self.left_len)
                    self.right_len = self.add_to_heap(max_left_heap_pop, right_minHeap, right_dict, self.right_len)
                else: continue
                    
            if i < k-1: continue        
            
            #updated maxleft heap and min right heap here:
            max_left_heap = self.pop_frm_heap(left_maxHeap, left_dict)*(-1)
            min_right_heap = self.pop_frm_heap(right_minHeap, right_dict)
            #print(max_left_heap, min_right_heap, i, left_dict, right_dict, self.left_len, self.right_len)
            
            #find median here
            if self.left_len > self.right_len:
                #if max_left_heap[0] exist
                median_list.append(max_left_heap)
            elif self.left_len == self.right_len:              
                median_list.append((max_left_heap + min_right_heap)/2)
                
        return median_list
            
    def pop_frm_heap(self, heap, curr_dict):
        while heap:
            if heap[0] not in curr_dict:
                heapq.heappop(heap)
            else:
                return heap[0]
    
    
    def add_to_heap(self, num, heap, curr_dict, curr_len):
        heapq.heappush(heap, num)
        curr_dict[num] = 1 if num not in curr_dict else curr_dict[num] + 1
        return curr_len + 1
        
    def remove_frm_heap(self, num, curr_dict, curr_len):
        #if num not in curr_dict: return True if num in right_dict else False
        curr_dict[num] -= 1
        if curr_dict[num] == 0:
            del curr_dict[num]
        return curr_len - 1
        
        
        
        