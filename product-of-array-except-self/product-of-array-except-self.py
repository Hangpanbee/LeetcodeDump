class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = [nums[0]]*len(nums)
        reverse_product_list = [nums[-1]]*len(nums)
        
        for i in range(1, len(nums)):
            product_list[i] = product_list[i-1]*nums[i]
        
        
        nums = nums[::-1]
        for i in range(1, len(nums)):
            reverse_product_list[i] = reverse_product_list[i-1]*nums[i]
        
        reverse_product_list = reverse_product_list[::-1]
        print(reverse_product_list)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = reverse_product_list[i+1]
            elif i == len(nums)-1:
                ans[i] = product_list[i-1]
            else:
                ans[i] = product_list[i-1]*reverse_product_list[i+1]
                
        return ans
            
        