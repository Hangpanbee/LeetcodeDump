class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        prev_num_tracker = {}
        
        ans = set()
        for num in nums:
            
            upper_target_num = k + num
            lower_target_num = num - k
            
            if upper_target_num in prev_num_tracker:
                ans.add((min(upper_target_num, num), max(upper_target_num, num) ) )
            if lower_target_num in prev_num_tracker:
                ans.add((min(lower_target_num, num), max(lower_target_num, num) ) )
            prev_num_tracker[num] = 1
          
        #print(prev_num_tracker)    
        return len(ans)
        