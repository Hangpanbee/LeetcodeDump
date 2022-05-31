class Solution:
    def decodeString(self, s: str) -> str:
        # similar to valid parenthesis
        
        stack = []
        
        for i, char in enumerate(s):
            if char == "]":
                currWord = []
                while stack and not type(stack[-1]) == int:
                    popped = stack.pop()
                    if popped == "[": continue
                    currWord.append(popped)
                multiplier = stack.pop()
                currWord.reverse()
                currWord = "".join(currWord*multiplier)
                stack.append(currWord)
            elif char.isdigit():
                if stack and type(stack[-1]) == int:
                    prevNum = stack.pop()
                    stack.append(prevNum*10+int(char))
                else:
                    stack.append(int(char))
            else:
                stack.append(char)
                
        return "".join(stack)
                