class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums)
        
        while i < len(nums):
            currNum = nums[i]
            
            if currNum < len(nums) and i != nums[i]:
                nums[currNum], nums[i] = nums[i], nums[currNum]
            
            #briliant
            else: i+=1
            
        
        for i in range(j):
            if i != nums[i]:
                return i
        return nums[-1]+1