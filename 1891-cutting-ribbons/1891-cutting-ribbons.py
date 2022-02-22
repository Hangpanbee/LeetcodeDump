class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def isPossible(ribbon_len):
            size = 0
            for ribbon in ribbons:
                size += ribbon//ribbon_len

                if size >= k:
                    return True
     
            return False
        
        l, r = min(ribbons)//k, sum(ribbons)//k
        while l < r:
            mid = l + (r-l+1)//2
            if isPossible(mid):
                l = mid
            else:
                r = mid - 1

                
        return l
        