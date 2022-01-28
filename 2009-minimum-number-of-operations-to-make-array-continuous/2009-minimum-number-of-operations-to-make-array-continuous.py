class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l, r = 0, 0
        nums.sort()
        #print(nums, len(nums))
        ans = 9999999999
        duplicate = 0
        while r < len(nums): 
            goal = nums[l] + len(nums) - 1
            if r-1 >= 0 and nums[r] == nums[r-1]:
                duplicate += 1
            if nums[r] > goal:
                ans = min(ans, len(nums) - r  + l  + duplicate)
                l += 1
                if nums[l] == nums[l-1]:
                    duplicate -= 1
                continue
            
                
            r += 1
   
        return min(ans, len(nums) - r + l + duplicate)
                
            
        