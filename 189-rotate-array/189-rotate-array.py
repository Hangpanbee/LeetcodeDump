class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0: return
        
        
        misplacedUnits = math.gcd(len(nums), k)
        
        for i in range(misplacedUnits):
            nextI = (i+k)%len(nums)
            misplacedVal = nums[i]
            while i != nextI:
                prev = nums[nextI]
                nums[nextI] = misplacedVal
                misplacedVal = prev
                nextI = (nextI+k)%len(nums)
                
            nums[nextI] = misplacedVal    
        
        