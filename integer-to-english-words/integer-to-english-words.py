class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        tenthToWord = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion", 5: "Quadrillion"}
        numToWord = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        ans = ""
        numLen = len(str(num))
        comma = (numLen)//3 
        def getHundrethToWord(num):
            toTheTenth = 2
            currNum = num
            _ans = ""
    
            _ans += "" if currNum//(100) == 0 else numToWord[currNum//(10**2)] + " Hundred" 
            currNum = currNum%(10**2)
            if currNum == 0:
                return _ans
            
            if len(_ans) > 0:
                _ans += " "
    
            if (currNum < 20):
                return _ans + numToWord[currNum]
            else:         
                _ans += numToWord[(currNum//10)*10]
                currNum = currNum%(10)
                _ans += "" if currNum == 0 else " " + numToWord[currNum]
                return _ans    
        
        
        ans = ""
        while (comma >= 0 and num != 0):
            
            currNum = num // (10**(3*comma))
            if len(ans) > 0 and currNum != 0:
                ans += " "
        
            ans += getHundrethToWord(currNum)
            if (comma > 0 and currNum != 0):
                ans += " " + tenthToWord[comma]
            num = num %(10**(3*comma) )
        
            comma -= 1
            
        return ans
                            
                            

                            
            