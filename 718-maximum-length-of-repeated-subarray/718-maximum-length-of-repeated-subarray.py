class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #  1 2 3 2 1        1 2 3
        #3 0 0 1 0 0    1 
        #2 0 1 0 2 0    2
        #1 1 0 0 0 3    3
        #4              4
        #7              7
        # brute force
        return self.getLongestCommonSubarray(nums1, nums2)
        
        
    def getLongestCommonSubarray(self, nums1, nums2):
        
        #nums1, nums2 = , len(nums1)
        dp = [[0]*(len(nums2)+2) for i in range(len(nums1)+2)]
    
        maxAns = 0
        for i1, v1 in enumerate(nums1):
            for i2, v2 in enumerate(nums2):
                if v1 == v2:
                    dp[i1+1][i2+1] = dp[i1][i2] + 1 
                    maxAns = max(maxAns, dp[i1+1][i2+1])
        return maxAns