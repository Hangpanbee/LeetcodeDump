
class Solution(object):
    def countSmaller(self, nums):
        for i, v in enumerate(nums):
            nums[i] = [v, i]
        ans = [0] * len(nums)
        
    
        def merge(left, right):
            l, r = 0, 0
            out = []
            prefix_sum = 0
            #print(left, right)
            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    out.append(left[l])
                    ans[left[l][1]] += prefix_sum
                    l+=1
                elif left[l][0] > right[r][0]:
                    out.append(right[r])
                    prefix_sum += 1
                    r+=1

            if r < len(right):
                out.extend(right[r:])
                #out += right[r:]
                
            while l < len(left):
                ans[left[l][1]] += prefix_sum
                out.append(left[l])
                l += 1

            #print(out)
            return out


        def mergeSort(nums):
            #the partition method
            if len(nums) == 1:
                return nums

            mid = len(nums)//2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)

        mergeSort(nums)
        return ans
        
        
        
