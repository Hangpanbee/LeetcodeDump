class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        while l < r:
            dist = r - l
            ans = max(ans, min(height[l], height[r])*dist)
            if height[l] > height[r]:
                r -= 1  
            elif height[l] < height[r]:
                l += 1
            else:
                r -= 1
                l += 1
        return ans
                
        