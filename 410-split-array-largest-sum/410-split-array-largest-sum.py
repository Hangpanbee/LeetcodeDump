class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPossible(diff_cap):
            count_m = 0
            total = 0
            for num in nums:
                total += num
                if total > diff_cap:
                    total = num
                    count_m += 1
                    if count_m >= m:
                        return False
            return True
        
        l, r = max(nums), sum(nums)

        while l < r:
            mid = l + (r-l)//2

            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
           
        return l