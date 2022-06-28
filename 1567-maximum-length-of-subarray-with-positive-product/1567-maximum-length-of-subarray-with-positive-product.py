class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        avoid odd number of - num
        -> longest window where count(neg)%2 == 0 && not include 0
        [1,-2,-3,4]
        [1,-2,]
        """
        
        l, r = 0, 0
        ans = 0
        
        negCount = 0
        #[0,1,-2,-3,-4]
        lastNeg = 0
        while r < len(nums):
            if nums[r] < 0:
                negCount += 1
                if negCount == 1: lastNeg = r
            elif nums[r] == 0:
                r+=1
                l=r
                negCount = 0
                continue
            
            if negCount%2 == 0:
                ans = max(ans, r-l+1)
            elif negCount%2 == 1:
                ans = max(ans, r-lastNeg)
            
            #r = 1
            r+=1
            
        # case of all positive or ending with only positive arrays
        return ans