class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        
        ## 4 questions to ask in binary question
        # 1. Use < or <=
        # 2. Use lower bound mid or upper bound mid
        # 3. How to process mid?
        # 4.
        
        ## should do this recursively tomorrow
        while l <= r:
            mid = l + (r-l)//2 
            if nums[mid] == target:
                lo, hi = mid, mid
                while lo > -1:
                    if nums[lo] == target: lo -= 1
                    else: break
                while hi < len(nums):
                    if nums[hi] == target: hi += 1
                    else: break
                return [lo+1, hi-1]
            elif nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
        return [-1, -1]