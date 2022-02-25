class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n == 1: return 1
        
        
        i_min, i_max = 2, (n+1)//2
        while i_min < i_max:
            mid = i_min + (i_max - i_min)//2
            isPossible = ((mid+1)*(mid))/2
 
            if isPossible >= n:
                i_max = mid
            elif isPossible < n:
                i_min = mid + 1
                
            
            
        return i_min
        