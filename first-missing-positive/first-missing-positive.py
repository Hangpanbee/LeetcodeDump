class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
       #bucket style
        for num in range(len(nums)):
            if nums[num] < 0:
                nums[num] = 0
                
    
        maxNum = max(nums)+1
        length = len(nums)
        for num in nums:
            
            modifiedNum = num % maxNum
            if modifiedNum > 0 and modifiedNum <= length:
                nums[modifiedNum-1] += maxNum
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] < maxNum:
                return i+1
         
        return maxNum
                

            
        
        
        
        
        