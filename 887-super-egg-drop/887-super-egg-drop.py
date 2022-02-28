class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1: return n
        
        i_min, i_max = 0, self.twoEggDrop(n)+1
        memoize = {}
        i = 0
        while i_min < i_max:
            mid = i_min + (i_max - i_min)//2
            max_range = self.recursive_range(k, mid, n, memoize)

            if max_range >= n:
                i_max = mid
            else:
                i_min = mid + 1
            i += 1
        
        return i_min
    
    def recursive_range(self, k, move, max_range, memoize):
        if (k, move) in memoize:
            return memoize[(k, move)]
        
        if k == 2:
            memoize[(k, move)] = self.base_range(move, max_range)
            return memoize[(k, move)]
        else:
            running_sum = 0
            curr_move = 1
            while running_sum < max_range and curr_move <= move:
                old_sum = self.recursive_range(k-1, move-curr_move, max_range, memoize) + 1   
                running_sum += old_sum
                curr_move += 1
            memoize[(k, move)] = running_sum
            return running_sum
                
      
        
    def base_range(self, move, max_range):
        if move == 0: return 0
        i_min, i_max = 1, max_range
        while i_min < i_max:
            mid = i_min + (i_max - i_min + 1)//2 
            curr_move = self.twoEggDrop(mid)
            if curr_move <= move:
                i_min = mid
            elif curr_move > move:
                i_max = mid - 1
                
        return i_min
    
    def twoEggDrop(self, n: int) -> int:
        if n == 1: return 1

        i_min, i_max = 2, n//2 + 1
        while i_min < i_max:
            mid = i_min + (i_max - i_min)//2
            isPossible = ((mid+1)*(mid))/2
 
            if isPossible >= n:
                i_max = mid
            elif isPossible < n:
                i_min = mid + 1
                
            
            
        return i_min