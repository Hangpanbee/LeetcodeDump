class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 1: return min(costs[0])
        smallest, second_smallest = 999999, 999999
        for cost in costs[0]:
            if cost < smallest:
                smallest, second_smallest = cost, smallest
              
            elif cost < second_smallest:
                second_smallest = cost
        
        
        for house in range(1, len(costs)):
            curr_smallest, curr_secnd_smallest = 9999999, 9999999
            for cost in range(len(costs[house])):
                if costs[house-1][cost] != smallest:
                    costs[house][cost] += smallest
                else:
                    costs[house][cost] += second_smallest
                
                if costs[house][cost] < curr_smallest:
                    curr_smallest, curr_secnd_smallest = costs[house][cost], curr_smallest
                    
                elif costs[house][cost] < curr_secnd_smallest:
                    curr_secnd_smallest = costs[house][cost]
            smallest, second_smallest = curr_smallest, curr_secnd_smallest
                
                    
        #print(costs)
        
        return smallest
                        
                
                
                
                    
            
        
        

        
        