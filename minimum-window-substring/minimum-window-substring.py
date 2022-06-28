class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        max_max = float('inf')
        a = self.count_table(t)
        counter = len(a)
        ans = ''
        while end < len(s):
        
            if s[end] in a:
                a[s[end]] -= 1
                if a[s[end]] == 0:
                    counter -= 1
            end += 1
        
            while counter == 0:
                #print(s[start:end], a, counter)
                if end-start < max_max: 
                    max_max = end-start
                    ans = s[start:end]
                if s[start] in a:
                    a[s[start]] += 1
                    if a[s[start]] > 0:
                        counter+=1
            
                start += 1
                
                    
        return ans
                
            
        
    def count_table(self, t):
        countnt = {}
        for i in t:
            if i in countnt:
                countnt[i] += 1
            else:
                countnt[i] = 1
        return countnt
        