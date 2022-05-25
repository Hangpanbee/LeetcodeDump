class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i, v in enumerate(nums):
            if v == 1: counts[1]+=1
            elif v == 2: counts[2]+=1
            elif v == 0: counts[0]+=1
        
 
        currColor = 0
        for i, v in enumerate(nums):
            while currColor < 3 and counts[currColor] == 0:
                currColor +=1
            nums[i] = currColor
            counts[currColor] -= 1