class Solution:

        
        
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        output_pre = self.getRow(rowIndex-1)
        output = [1] * (rowIndex+1)
        for i in range(1, len(output)-1):
            output[i] = output_pre[i-1] + output_pre[i]
        return output