class Solution:
    def __init__(self):
        self.ans_list = []
  
    
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        combination = ''

        if len(digits) == 0: return []
        self.recurCombination('', digits, letter)
        return self.ans_list
        
  
        
    def recurCombination(self, combination, digits, letter):
        #basecase is when there is no more letter to check
        if len(digits) == 0:
       
            self.ans_list.append(combination)
        else:
            for i in letter[digits[0]]:
                self.recurCombination(combination+i, digits[1:], letter)
        
        