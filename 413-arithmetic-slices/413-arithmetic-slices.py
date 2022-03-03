class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
 
        curr_diff = nums[1] - nums[0]
        l, r = 0, 1
        ans = 0
        while r < len(nums):
            if (nums[r] - nums[r-1]) != curr_diff:
                curr_diff = nums[r] - nums[r-1]
                l = r-1
                r+=1
                continue
            
            if (r-l+1) >= 3:
                ans += (r-l+1) - 3 + 1
            r+=1
        
        
        
        
        return ans
        