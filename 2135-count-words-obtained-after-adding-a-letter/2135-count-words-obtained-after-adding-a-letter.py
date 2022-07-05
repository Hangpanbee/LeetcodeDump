class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = {}
        for word in startWords:
            hashedWord = self.getHashedWord(word)
            seen[hashedWord] = True
            
        return self.getHashMaskingMap(seen, targetWords)
        
    
    def getHashedWord(self, word):
        primes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101)
        getHashChar = lambda x: primes[ord(x) - ord('a')]
        runningHash = 1
        for char in word:
            runningHash *= getHashChar(char)
        return runningHash
            
            
    def getHashMaskingMap(self, seen, targetWords: List[str]) -> int:
        primes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101)
        """
        practically doing bitmasking
        """
        getHashChar = lambda x: primes[ord(x) - ord('a')]
        hashedWords = []
        for word in targetWords:
            hashedWord = self.getHashedWord(word)
            hashedWords.append(hashedWord)
        ans = 0
        for i, hw in enumerate(hashedWords):
            for char in targetWords[i]:
                hashedChar = getHashChar(char)
                maskedWord = hw//hashedChar
                if maskedWord in seen: 
                    ans += 1
                    break
        return ans
                    