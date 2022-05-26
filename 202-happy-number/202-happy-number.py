class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        
        while n > 1:
            if n in seen: return False
            nxtN = 0
            _n = n
            
            for i in range(9, -1, -1):
                #print(i, _n//10**i, _n)
                nxtN += (_n//10**i)**2
                _n = _n%10**i
            seen[n] = True
            n = nxtN
            #print(n)
        return n == 1