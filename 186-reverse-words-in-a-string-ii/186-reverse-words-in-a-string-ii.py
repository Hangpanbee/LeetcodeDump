class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseWord(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
        
        """
        -> ["eulb si yks eht"]
        """
        
        reverseWord(0, len(s)-1)
        
        beginWord = 0
        for endWord in range(len(s)+1):
            
            if endWord == len(s)-1:
                reverseWord(beginWord, endWord)
            elif endWord < len(s) and s[endWord] == " ":
                reverseWord(beginWord, endWord-1)
                beginWord = endWord+1
                
        
        
        
        
        
        
    