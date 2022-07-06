class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1: return []
        
        
        ans = []
        curr_sum = 0
 
        for num in range(2, finalSum+2, 2):
            curr_sum += num
            left_over = finalSum - curr_sum
            ans.append(num)

            if left_over == 0:
                return ans
            
            if 0 < (left_over/2)-2 <= num:
                ans.append(left_over)
                return ans
            elif left_over/2 - 2 < 0:
                curr_sum -= num
                ans = ans[:len(ans)-1]
        
        return ans
            
        