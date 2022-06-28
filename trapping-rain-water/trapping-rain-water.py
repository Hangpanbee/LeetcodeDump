class Solution:
    def trap(self, height: List[int]) -> int:
        
        sumWaterTrapped = 0
        mono_stack = []


        for bar in range(len(height)):
            #decreasing stack
            while mono_stack and height[bar] > height[mono_stack[-1]]:
                poppedBarIndex = mono_stack.pop()
                poppedBar = height[poppedBarIndex]
                if not len(mono_stack): break
                #if there is only one ele that is smaller than height bar, which means there is no puddle formed
                tall = min(height[bar], height[mono_stack[-1]]) - poppedBar
                length = bar - mono_stack[-1] - 1
                
                sumWaterTrapped += tall*length

            mono_stack.append(bar)
            
        return sumWaterTrapped