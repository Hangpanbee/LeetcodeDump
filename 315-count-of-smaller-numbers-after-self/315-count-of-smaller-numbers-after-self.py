class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        binary search way
        """
        ans = [-1]*len(nums)
        newNums = []
        for i in range(len(nums)-1, -1, -1):
            ans[i] = self.update(newNums, nums[i])
            
        return ans
        
        
        
    def update(self, nums, target):
        nI = bisect.bisect_left(nums, target)
        nums.insert(nI, target)
        
        return nI