class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        counter = collections.defaultdict(set)
        for word in dict:
            word = list(word)
            for i in range(len(word)):
                newWord = word[0:i] + word[i+1: len(word)]
                newWord = ''.join(newWord)
                counter[i].add(newWord)
        #print(counter)
        for ans in counter.values():
            if len(ans) < len(dict):
                return True
        return False
            
        