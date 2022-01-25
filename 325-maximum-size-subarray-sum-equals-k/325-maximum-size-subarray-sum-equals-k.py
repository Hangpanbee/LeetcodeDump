class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        sum_tracker = {}
        cumu_sum = 0
        
        for i, v in enumerate(nums):
            cumu_sum += v
            sum_tracker[cumu_sum] = i

        
        running_sum = 0
        ans = 0
        for i, v in enumerate(nums):
            if (running_sum + k) in sum_tracker:
                ans = max(ans, sum_tracker[running_sum+k] - i + 1)
            running_sum += v
            if running_sum in sum_tracker and sum_tracker[running_sum] == i: 
                del sum_tracker[running_sum] 

        return ans
                
            
        