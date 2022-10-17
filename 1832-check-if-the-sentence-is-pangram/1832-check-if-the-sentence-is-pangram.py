class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_sentence = set(sentence)
        
        return len(set_sentence) == 26