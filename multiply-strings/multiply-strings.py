class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1, int2 = 0, 0
        for i,v in enumerate(num1):
            int1 += (ord(v) - ord('0')) * 10**(len(num1)-i-1)
        
        for i,v in enumerate(num2):
            int2 += (ord(v) - ord('0')) * 10**(len(num2)-i-1)
        

        return str(int1*int2)
            