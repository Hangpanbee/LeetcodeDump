class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majorityElement = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num == majorityElement:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                majorityElement = num
                count = 1
                
        return majorityElement