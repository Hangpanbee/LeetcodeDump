import math
class Solution:
    def numSquares(self, n: int) -> int:
        memoize = {}
        self.global_min = 9999999
        def dp(n, sq):
            if n >= 0 and n < 3: 
                self.global_min = min(self.global_min, sq+n)
                return sq+n

            
            if sq > self.global_min: return 99999999
            max_choice = int(math.sqrt(n))
            
            memoize[n] = 9999999
            for choice in range(max_choice, 0, -1):
                left_over = n % choice**2
                curr_sq = n // choice**2
                memoize[n] = min(memoize[n], dp(left_over, sq+curr_sq))

            return memoize[n]

        dp(n, 0)
        return self.global_min
        
        
                
            