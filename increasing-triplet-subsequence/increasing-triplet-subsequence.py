class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [-99999999999]+[9999999999]*3
        curr_target = 0
        
        for i in range(len(nums)):
            if nums[i] > dp[curr_target]:
                dp[curr_target + 1] = min(dp[curr_target+1], nums[i])
                curr_target += 1
                if curr_target == 3: return True
            else:
                #if the current number is smaller than the current count:
                    #then find where that numbers can count to
                for j in range(0, curr_target+1):
                    if nums[i] <= dp[j]:
                        dp[j] = nums[i]
                        break
            
 
        return False
                