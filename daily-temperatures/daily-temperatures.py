class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mono_stack = []
        ans = [0] * len(temperatures)
        for currDay, currTemp in enumerate(temperatures):
            
            while mono_stack and temperatures[mono_stack[-1]] < currTemp:
                poppedDay = mono_stack.pop()
                ans[poppedDay] = currDay - poppedDay
                
            mono_stack.append(currDay)
        
        return ans
        