class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        mapWordToFreq = {}
        maxFreq = 0
        for word in words:
            if word not in mapWordToFreq:
                mapWordToFreq[word] = 0
            mapWordToFreq[word] += 1
            maxFreq = max(maxFreq, mapWordToFreq[word])

            
        bucketSort = [[] for i in range(maxFreq+1) ]
        for word, freq in mapWordToFreq.items():
            bucketSort[freq].append(word)
        
        ans = []
        freq = maxFreq
        while freq > 0 and len(ans) < k:
            words = bucketSort[freq]
            if len(words) >= 2:
                words.sort()
            ans.extend(words)
            if len(ans) >= k: break
            freq -= 1
        
        
        return ans[:k]