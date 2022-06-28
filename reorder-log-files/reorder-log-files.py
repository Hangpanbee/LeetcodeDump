class Solution:
    def compare(self, l1, l2):
        l1 = l1.split(" ")
        l2 = l2.split(" ")
        i = 1
        while i < len(l1) and i < len(l2):
            if l1[i] > l2[i]: return 1
            elif l1[i] < l2[i]: return -1
            i+=1
        
        if len(l1) > len(l2): return 1
        elif len(l1) < len(l2): return -1
        
        for i in zip(l1[0], l2[0]):
            if i[0] > i[1]:
                return 1
            elif i[0] < i[1]:
                return -1
        
        return 1 if len(l1[0]) > len(l2[0]) else -1
    
    def getLetterAndDigit(self, logs):
        letterLog = []
        digitLog = []
        for i, v in enumerate(logs):
            if v[1].isdigit():
                digitLog.append(" ".join(v))
            else:
                letterLog.append(" ".join(v))
        return (letterLog, digitLog)
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [log.split(" ") for log in logs]
        
        letterLog, digitLog = self.getLetterAndDigit(logs)
        sortedLetterLog = sorted(letterLog, key=functools.cmp_to_key(self.compare))
        
        return sortedLetterLog + digitLog
        