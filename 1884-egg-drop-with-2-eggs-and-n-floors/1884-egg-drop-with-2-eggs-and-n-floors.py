class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n == 1: return 1
        
        def isPossible(n_max):
            running_sum = 0
            while running_sum < n:
                if n_max == 0: return False
                running_sum += n_max
                n_max -= 1
 
            return True
        
        i_min, i_max = 2, (n+1)//2
        while i_min < i_max:
            mid = i_min + (i_max - i_min)//2
            if isPossible(mid):
                i_max = mid
            elif not isPossible(mid):
                i_min = mid + 1
                
            
            
        return i_min
        