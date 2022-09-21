class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        curr_even_num = 0
        for num in nums:
            if num%2==0:
                curr_even_num += num
                
        ans = []
        for val, index in queries:
            curr_num = nums[index]
            nxt_num = nums[index] + val
            
            if curr_num%2==1 and nxt_num%2==1:
                pass
            elif curr_num%2==1 and nxt_num%2==0:
                curr_even_num += nxt_num
            elif curr_num%2==0 and nxt_num%2==1:
                curr_even_num -= curr_num
            elif curr_num%2==0 and nxt_num%2==0:
                curr_even_num -= (curr_num - nxt_num)
            
            nums[index] = nxt_num
            
            ans.append(curr_even_num)
        
        return ans