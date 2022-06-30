class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charBucket = [collections.deque() for i in range(26)]
        """
        run time: worst case: o(m*n) -> m
        """
        for i, w in enumerate(words):
            charBucket[ord(w[0]) - ord('a')].append((i, 0))
        
        ans = 0
        for i, char in enumerate(s):
            ordChar = ord(char) - ord('a')
            
            
            lenChar = len(charBucket[ordChar])
            i = 0
            while i < lenChar:
                #print(pointer, charBucket[ordChar])
                w, currP = charBucket[ordChar].popleft()
                word = words[w]
                if (currP + 1) == len(word): 
                    ans += 1
                else:
                    nxtOrd = ord(word[currP+1]) - ord('a')
                    charBucket[nxtOrd].append((w, currP+1))
                i+=1
            
        return ans
        