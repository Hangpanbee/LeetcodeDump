class Solution:
    def climbStairs(self, n: int) -> int:
        waysToClimb = {}
        # ways to climb from top up
        def helper(m):
            if m == 0: return 1
            if m == 1: return 1
            if m in waysToClimb: return waysToClimb[m]
            waysToClimb[m] = helper(m-1) + helper(m-2)
            return waysToClimb[m]
        
        return helper(n)
        
        