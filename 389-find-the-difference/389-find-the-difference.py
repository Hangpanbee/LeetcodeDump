class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sum(ord(i) for i in s)
        b = sum(ord(i) for i in t)
        return chr(abs(a-b))
        