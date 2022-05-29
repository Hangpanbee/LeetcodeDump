class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        """
        "avavadvddee"
        """
        
        totalEqualCountS = 0
        for numOfUnique in range(1, 26+1):
            totalEqualCountS += self.substringUniqueChar(s, numOfUnique, count)

        return totalEqualCountS
            
            
    def substringUniqueChar(self, s, unique, count):
        l, r = 0, 0
        mapCharToFreq = {}
        equalCountS = 0
        while r < len(s):
            if s[r] not in mapCharToFreq:
                mapCharToFreq[s[r]] = 0
            mapCharToFreq[s[r]] += 1
           # -> r = 1, mapCharToFreq = {a: 1, v:1} 
            while mapCharToFreq[s[r]] > count:
                mapCharToFreq[s[l]] -= 1
                if mapCharToFreq[s[l]] == 0: 
                    del mapCharToFreq[s[l]]
                l+=1
        
            while len(mapCharToFreq) > unique:
                mapCharToFreq[s[l]] -= 1
                if mapCharToFreq[s[l]] == 0:
                    del mapCharToFreq[s[l]]
                l += 1
            # -> l = 1, mapCharToFreq = {v:1}
            if len(mapCharToFreq) == unique:
                isEqualCount = True
                for i, v in mapCharToFreq.items(): 
                    if unique == 1 and v < count:
                        isEqualCount = False
                    elif v != count:
                        isEqualCount = False

                if isEqualCount == True: equalCountS += 1
            r+=1
        
        return equalCountS