class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        dictRep = {i: "" for i in range(numRows)}

        rowMap, direction = 0, 1
        for index, letter in enumerate(s):
            dictRep[rowMap] += letter
            
            rowMap += direction
            if rowMap >= numRows: rowMap, direction = numRows-2, -1
            elif rowMap < 0: rowMap, direction = 1, 1
                
        return "".join(dictRep.values())
            