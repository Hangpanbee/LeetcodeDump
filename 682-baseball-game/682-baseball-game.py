class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                curr_score = stack[-1]*2
                stack.append(curr_score)
            elif op == "+":
                curr_score = stack[-1] + stack[-2]
                stack.append(curr_score)
            else:
                stack.append(int(op))
                
        return sum(stack)