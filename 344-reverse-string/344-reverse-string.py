class Solution:
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(s, l, r):
            if l >= r: return
            s[l], s[r] = s[r], s[l]
            helper(s, l+1, r-1)
        helper(s, 0, len(s)-1)


        