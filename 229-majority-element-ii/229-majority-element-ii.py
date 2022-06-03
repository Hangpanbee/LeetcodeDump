class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        can1, can2 = None, None
        c1, c2 = 0, 0
        for n in nums:
            if can1 == n:
                c1 += 1
            elif can2 == n:
                c2 += 1
            elif c1 == 0:
                can1 = n
                c1 += 1
            elif c2 == 0:
                can2 = n
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
                
        #print(can1, can2)
        ans = []
        for can, c in [(can1, c1), (can2, c2)]:
            if nums.count(can) <= len(nums)//3: continue
            ans.append(can)
        
        return ans