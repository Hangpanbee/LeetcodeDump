class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, v in enumerate(tokens):
           
            if (v[0] == "-" and len(v) >1) or v.isdigit(): 
                stack.append(int(v))
            else:
                n1, n2 = stack.pop(), stack.pop()
                if v == "+": stack.append(n1+n2)
                elif v == "-": stack.append(n2-n1)
                elif v == "*": stack.append(n1*n2)
                elif v == "/":
                    if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
                        stack.append(ceil(n2/n1))
                    else:
                        stack.append(floor(n2/n1))
                       
                        
                        
        return stack[-1]
                        