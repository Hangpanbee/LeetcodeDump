class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        for words quesiton, ask if only consist of lowercase and symbol
        edge case: wher one 1 word fits in a line
        what if a word is longer than maxWidth????
        
        """
        getWordsLen = lambda wordsInline: sum(len(word) for word in wordsInline)
        
        def getWordsPerLine(start):
            wordsInline, width = [], 0
            
            for i in range(start, len(words)):
                word = words[i]
                if len(wordsInline) + len(word) + width <= maxWidth:
                    wordsInline.append(word)
                    width += len(word)
                else:
                    return (i, wordsInline)
            return (len(words), wordsInline)
                
        def evenJustify(wordsInline):
            sumLen = getWordsLen(wordsInline)
            spaces = maxWidth - sumLen
            spaceLots = 1 if len(wordsInline) == 1 else len(wordsInline)-1
            spacePerLot = spaces//spaceLots
            spaceArr = [spacePerLot]*spaceLots
            
            for extraSpace in range(spaces%spaceLots):
                spaceArr[extraSpace] += 1
            
            justifiedLine = []
            for s, w in zip(spaceArr, wordsInline):
                justifiedLine.append(w)
                justifiedLine.append(s*" ")
            
            if len(wordsInline) > 1:
                justifiedLine.append(wordsInline[-1])
            
            return "".join(justifiedLine)
        
        def leftJustify(wordsInline):
            sumLen = getWordsLen(wordsInline)
            spaces = maxWidth - sumLen
            justifiedLine = []
            for word in wordsInline:
                justifiedLine.append(word)
                if spaces > 0: justifiedLine.append(" ")
                spaces -= 1
     
            if spaces > 0:
                justifiedLine.append(" "*spaces)
            
            return "".join(justifiedLine)
        
        
        i = 0
        text = []
        while i < len(words):
            nxtI, currWordsInLine = getWordsPerLine(i)
            text.append(currWordsInLine)
            i = nxtI
        
        
        for line in range(len(text)-1):
            text[line] = evenJustify(text[line])
        
        text[-1] = leftJustify(text[-1])
        #print(len(text[-1]))
        return text