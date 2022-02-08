class Solution:
    def addDigits(self, num: int) -> int:
        
        
        while len(str(num)) > 1:
            new_num = 0
            for i in str(num):
                new_num += int(i)
                
            num = new_num
            
        return num
        