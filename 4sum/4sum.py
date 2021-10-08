class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
       
        ans = set()
        nums.sort()
        # [-2, -1, 0, 0, 1, 2]
        
        
        
        for num1 in range(len(nums)):
            for num2 in range(num1+1, len(nums)):
                l, r = num2+1, len(nums)-1
                
                while l < r:
                    currSum = nums[l] + nums[r] + nums[num1] + nums[num2]
                    
                    if currSum == target:
                        ans.add((nums[num1], nums[num2], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif currSum < target:
                        l += 1
                    elif currSum > target:
                        r -= 1
                        
        return ans
        