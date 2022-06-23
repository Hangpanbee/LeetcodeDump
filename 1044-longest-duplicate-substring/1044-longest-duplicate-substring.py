class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """
            B A N A N A
        B   0 0 0 0 0 0
        A     0 0 1 0 1  
        N       0 0 2 0
        A         0 0 3  
        N           0 0
        A             0 
        
        """
        m = len(s)
        BASE, MOD = 101, 1_000_000_000_001
        hashS = [0] * (m+1)
        POW = [1]*(m+1)
        for i in range(m): POW[i+1] = POW[i] * BASE % MOD
        for i in range(m): hashS[i+1] = (hashS[i]*BASE + (ord(s[i]) - 97) ) % MOD
        
        def getHash(h, left, right):  # 0-based indexing, right inclusive
            return (h[right + 1] - h[left] * POW[right - left + 1] % MOD + MOD) % MOD        
    
        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(m - size + 1):
                h = getHash(hashS, i, i + size - 1)
                seen[h] = i
            for i in range(m - size + 1):
                h = getHash(hashS, i, i + size - 1)
                if h in seen and seen[h] != i:
                    return (i, i+size)
            return ()
        
        left, right = 1, m
        st, e = -1, -1
        while left <= right:
            mid = (left + right) // 2
            isFound = foundSubArray(mid)
            if isFound:
                st, e = isFound  # Update answer
                left = mid + 1  # Try to expand size
            else:
                right = mid - 1  # Try to shrink size
            
        return s[st:e] if st != -1 else ""