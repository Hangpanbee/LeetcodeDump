class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
            
        self.ans = 0  
            
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            
            left = mergeSort(nums[:len(nums)//2])
            right = mergeSort(nums[len(nums)//2:])

            return merge(left, right)
            

        def merge(left, right):
            out = []
            l, r = 0, 0

            while r < len(right):

                self.ans += len(left) - bisect.bisect_right(left, right[r]*2, l, len(left))
                r += 1
            
            r = 0
            while l < len(left) and r < len(right):
                if left[l] >= right[r]:
                    out.append(right[r])
                    r+=1
                elif left[l] < right[r]:
                    out.append(left[l])
                    l+=1
 
            #print(self.ans)
            if l < len(left):
                out += left[l:]
                #out.extend(left[l:])
            if r < len(right):
                out += right[r:]
                #out.extend(right[r:])
         
            return out
        
        mergeSort(nums)
        return self.ans
                