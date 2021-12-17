class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lower, upper = 0, 0
        odd_count = 0
        ans = 0

        while upper < len(nums):
            
            if nums[upper]%2==1:
                odd_count += 1
             
            if odd_count == k:
                right_side, left_side = 1, 1
            else:
                right_side, left_side = 0, 0
                
            while odd_count == k and upper < (len(nums)-1): 
                if nums[upper+1]%2==1:
                    break
                right_side += 1
                upper += 1
                            
                    
      
            while odd_count == k and lower <= upper:
                
                if nums[lower]%2==1:
                    lower+=1
                    odd_count -= 1
                    break
                left_side += 1
                lower += 1
            print(left_side, right_side)
            ans += left_side*right_side    
            
            upper += 1
            
        return ans
            
