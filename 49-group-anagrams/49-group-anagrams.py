class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        are the words unique?
        runtime: 
        """
        
        mapHashToGroup = collections.defaultdict(list)
        for i, s in enumerate(strs):
            hashValue = self.calHash(s)
            mapHashToGroup[hashValue].append(s)            
        
        
        
        return mapHashToGroup.values()
    
    def calHash(self, string):
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
        hashValue = 1
        m = 10**9+7
        for char in string:
            hashValue *= primes[ord(char) - 97]
        return hashValue % m