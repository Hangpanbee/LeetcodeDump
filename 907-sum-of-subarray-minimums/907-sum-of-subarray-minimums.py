class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        PLE = [-1]*len(arr)
        NLE = [len(arr)]*len(arr)
        

        #(3,0)(4,3)(7,1)(8,2)
        #(8,2)(7,1)(4,3)(3,0)
        #NLE = [-1,3,4,-1]
        #PLE = [-1,0,1,0]
        
        #   3 4 7 8
        # [3] [4] [7] [8]
        # [3,4] [4,7] [7,8]
        # [3,4,7] [4,7,8]
        # [3,4,7,8]
        # -> 3*4 + 4*3 + 7*2 + 8*1
        
        #   8 7 4 3
        # [8] [7] [4] [3]
        # [8,7] [7,4] [4,3]
        # [8,7,4] [7,4,3]
        # [8,7,4,3]
        # -> 8*1 + 7*2 + 4*3 + 3*4
        
        #   8 7 3 4
        # [8] [7] [3] [4]
        # [8,7] [7,3] [3,4]
        # [8,7,3] [7,3,4]
        # [8,7,3,4]
        # -> 8*1 + 7*2 + 3*6+4 = 8+14+18+4
        #PLE=[-1,-1,-1,2]
        #NLE=[1,2,4,4]
        # -> 8*(0-0)+1*1) + 7*(1-0+1)*1) + 3*(2-0+1)*(4-2) + 4*(4-(2+1))
        
        # using sorted does work but that would make it o(nlogn)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
                #stack = []
            if stack: 
                PLE[i] = stack[-1]
            stack.append(i)
            # [-1,-1,-1, 2]
        
        stack = []
        for i in range(len(arr)-1, -1, -1):
            # arr[i] = 4
            # arr[i] = 3
            # arr[i] = 7
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            #stack = []
            if stack:
                NLE[i] = stack[-1]
            #   [1,2,4,4]
            #   
            stack.append(i)
        
        ans = 0
        #PLE=[-1,-1,-1,-1,3]
        #NLE=[1,2,4,4]
        for i, v in enumerate(arr):
            # i, v = 0, 8
            
            ans += v*(i-PLE[i])*(NLE[i]-i)
            # ans = (0--1)*(1-0) = 1
            # ans = ()
            
            
        m = 10**9+7
        return ans % m 
            