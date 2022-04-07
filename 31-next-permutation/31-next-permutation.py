class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        def binarySearch(l, r, target):
            while l < r:
                mid = l + (r-l+1)//2 
                #print(mid)
                if nums[mid] <= target:
                    r = mid - 1
                elif nums[mid] > target:
                    l = mid 
            print(l)
            return l
        
        def inplace(l): 
            midPoint = (len(nums) - l)//2
            for i in range(midPoint):
                nums[l+i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[l+i]
            
            
        pivot2 = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                pivot = binarySearch(i+1, len(nums)-1, nums[i])

                pivot2 = i
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        if pivot2 == -1:
            return nums.sort()
        else:
            inplace(pivot2+1)
            return nums

            

 
         