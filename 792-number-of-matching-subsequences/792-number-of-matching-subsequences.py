class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charBucket = [[] for i in range(26)]
        
        for i, w in enumerate(words):
            charBucket[ord(w[0]) - ord('a')].append((i, 0))
        
        ans = 0
        for i, char in enumerate(s):
            ordChar = ord(char) - ord('a')
            
            charBucketCopy = charBucket[ordChar].copy()
            charBucket[ordChar] = []
            for j, pointer in enumerate(charBucketCopy):
                #print(pointer, charBucket[ordChar])
                w, currP = pointer
                word = words[w]
                if (currP + 1) == len(word): 
                    ans += 1
                else:
                    nxtOrd = ord(word[currP+1]) - ord('a')
                    charBucket[nxtOrd].append((w, currP+1))
            
        return ans
        