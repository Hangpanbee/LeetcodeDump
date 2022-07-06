class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
            a b c c b 
        a   1 1 1  
        b     1 1 2 3
        c       1 2
        {a: 0, b: 1, c: 1}
        
        """
        getCharOrd = lambda x: ord(x) - ord('a')
        charBucket = collections.defaultdict(list)
        for i, v in enumerate(source):
            charBucket[v].append(i)
        
        copy = 1
        sI = -1
        
        for i, char in enumerate(target):
 
            if char not in charBucket: return -1
            nxtI = bisect.bisect_right(charBucket[char], sI)
            if (nxtI) == len(charBucket[char]):
                copy += 1
                sI = charBucket[char][0]
            else:
                sI = charBucket[char][nxtI]

            
        
            
        return copy