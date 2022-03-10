

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        
        def helper(nums):
            isNonCoprime = True
            l, r = 0, 1
            while r < len(nums):
                
                if math.gcd(nums[l], nums[r]) > 1:
                    nums[l] = math.lcm(nums[l], nums[r])
                    nums[r] = 0
                else:
                    l = r
                r += 1
             
            ans = []
            for num in nums:
                if num != 0:
                    ans.append(num)

            return isNonCoprime,ans
        
        isDone, nums = [False, nums]
        #print(isDone[0])
        
        isDone, ans = helper(nums)
        isDone, ans  = helper(ans[::-1])
        isDone, ans = helper(ans[::-1])
        isDone, ans = helper(ans[::-1])

        
        return ans[::-1]
            
        
    
        
        
        

  

        