class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        from collections import deque
        q = deque()
        ans = []
        for i, nu in enumerate(nums):
            while q and nums[q[-1]] < nu:
                q.pop()
            q.append(i)
            #take the left most element out when it is out of the window
            if q[0] == i-k:
                q.popleft()
            #append the biggest value and the biggest value is always at the beginning
            if i >= k-1:
                ans.append(nums[q[0]])
        return ans