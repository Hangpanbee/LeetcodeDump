class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupTracker = {}
        
        for num in nums:
            if num in dupTracker: return True
            else: dupTracker[num] = 1
        
        return False
        