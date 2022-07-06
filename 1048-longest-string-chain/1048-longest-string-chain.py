class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ansDict = {}
        maxAns = 1
 
        
        for word in sorted(words, key = len):
            ansDict[word] = 1
            #dissect the word:
            for j in range(len(word)):
                rmvWord = word[:j] + word[j+1::]
                if rmvWord in ansDict:
                    ansDict[word] = max(ansDict[rmvWord] + 1, ansDict[word])
                    maxAns = max(maxAns, ansDict[word])          
        return maxAns
        