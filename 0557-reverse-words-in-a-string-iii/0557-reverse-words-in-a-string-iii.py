class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        for i, v in enumerate(s_list):
            s_list[i] = self.reverseWord(v)
        
        return " ".join(s_list)
            
        
    def reverseWord(self, word: str) -> str:
        return word[::-1]