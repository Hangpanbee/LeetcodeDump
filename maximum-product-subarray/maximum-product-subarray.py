class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        #print(dp)
        max_val = 0
        prev_state_min, prev_state_max = 0, 0
        for i in range(len(nums)):
            #min_val
            a = min(prev_state_min*nums[i], prev_state_max*nums[i], nums[i])
            b = max(prev_state_min*nums[i], prev_state_max*nums[i], nums[i])
            
            
            prev_state_min, prev_state_max = a, b
            max_val = max(prev_state_max, max_val)
        #print(dp)   
        return max_val
        