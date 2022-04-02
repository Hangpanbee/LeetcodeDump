class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        new_string_left = ""
        new_string_right = ""
        skipahead = 0
        while l < r:
            if s[l] != s[r]:
                new_string_left = s[0:l] + s[l+1:len(s)]
                new_string_right = s[0:r] + s[r+1:len(s)]
                break
            l += 1
            r -= 1
        #print(new_string_left)
        return self.palidromecheck(new_string_left) or self.palidromecheck(new_string_right)
    
    def palidromecheck(self, s):
        l, r = 0, len(s)-1
        
        while l < r:
            if s[l] != s[r]:
                #print(s[l], s[r], l, r)
                return False
            l+=1
            r-=1
        return True
        