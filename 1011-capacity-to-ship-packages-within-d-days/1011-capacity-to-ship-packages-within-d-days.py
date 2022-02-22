class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isPossible(weight_capacity):
            total = 0
            day = 0
            for weight in weights:
                
                total += weight

                if total > weight_capacity:
                    total = weight
                    day += 1

                    if day >= days:
                        return False
            return True
            
            
        #search_space
        l, r = max(weights), sum(weights)
        
        while l < r:
            mid = l + (r-l)//2
           # print(mid, isPossible(mid))
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
                
        return l