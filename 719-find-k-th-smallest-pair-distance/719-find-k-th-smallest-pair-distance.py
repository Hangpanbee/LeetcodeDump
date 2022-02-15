class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, r = 0, len(nums)-1
        upper_range = nums[r] - nums[l]
        lower_range = 0
        while lower_range < upper_range:
            mid = lower_range + (upper_range-lower_range)//2
            count = self.count_smaller_val(mid, nums)

            
            if count >= k :
                upper_range = mid
            elif count < k:
                lower_range = mid + 1
            
            
        return lower_range
            
    
    def count_smaller_val(self, compared_val, nums):
        count = 0
        col = len(nums)-1
        for row in range(len(nums)-1, -1, -1):
            
            while col < len(nums):
                if (nums[col] - nums[row]) <= compared_val:
                    count += col - row
                    break   
                else:
                    col -= 1
        return count
                
        
        