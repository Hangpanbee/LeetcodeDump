class Solution:
    def reverse(self, x: int) -> int:
        '''
        If y = 10^x, then log(y) = x
        Which means we can find the len of a number through this trick without converting it         to string 
        number is not iterable so the trick is to do a while loop checking if it is not 0
        
        '''
        ans, remaining_x, sign = 0, abs(x), 1 if x > 0 else -1
        while remaining_x:
            ans = ans*10 + remaining_x%10
            remaining_x = remaining_x//10
        return ans*sign if -2**31 < ans*sign < 2**31-1 else 0
        