class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def partition(nums, l, r):
            midIndex = l + (r-l)//2
            nums[r], nums[midIndex] = nums[midIndex], nums[r]
            
            i = l 
            pivot = nums[r]
            
            
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
            
            
        def quickSort(nums, l, r):
            if l >= r: return 
            
            
            
            p = partition(nums, l, r)
            
            quickSort(nums, l, p-1)
            quickSort(nums, p+1, r)
            
        
        quickSort(nums, 0, len(nums)-1)
        
        return nums