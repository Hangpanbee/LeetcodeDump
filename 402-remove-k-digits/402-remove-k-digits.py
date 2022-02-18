class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        num = num+"0"
        mono_stack = []
        
        for i in range(len(num)):
            while mono_stack and mono_stack[-1] > num[i] and k > 0:
                mono_stack.pop()
                k -= 1
            
      
            mono_stack.append(num[i])
        
        nonzero_index = 0
        while nonzero_index < len(mono_stack) and mono_stack[nonzero_index] == "0":
            nonzero_index += 1
        

        return "".join(mono_stack[nonzero_index:(len(mono_stack)-1)]) if nonzero_index < len(mono_stack) else "0"
        