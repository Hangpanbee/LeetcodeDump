class Solution:
    def romanToInt(self, s: str) -> int:
        romanArray = [1, 5, 10, 50, 100, 500, 1000]
        symbolArray = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
        currRoman = symbolArray[s[-1]]
        i = len(s)-1
        ans = 0
        # ex: LIV, currI = 1, i = 2, ans = 0
        
        while i >= 0:
            if symbolArray[s[i]] < currRoman:
                ans -= romanArray[symbolArray[s[i]]]
                # ans = 4
            elif symbolArray[s[i]] >= currRoman:
                currRoman = symbolArray[s[i]]
                ans += romanArray[currRoman]
            # ans = 4, i = 0
            
            i -= 1
            
        return ans