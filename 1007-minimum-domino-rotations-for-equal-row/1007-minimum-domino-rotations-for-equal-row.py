class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        
        choice1, isChoice1 = tops[0], True
        choice2, isChoice2 = bottoms[0], True
        
        for i, j in zip(tops, bottoms):
            if i != choice1 and j != choice1:
                isChoice1 = False
            if i != choice2 and j != choice2:
                isChoice2 = False
        ans = 9999999999
        
        if not isChoice1 and not isChoice2:
            return -1
        
        if isChoice1:
            ans = min(len(tops)-tops.count(choice1), len(bottoms)-bottoms.count(choice1))
        if isChoice2:
            ans = min(len(tops)-tops.count(choice2), len(bottoms)-bottoms.count(choice2))
        
        return ans
            
            
        