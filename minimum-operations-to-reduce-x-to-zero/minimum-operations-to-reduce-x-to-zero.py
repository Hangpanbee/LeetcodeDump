class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        sum_at_each_position = {0: 0}
        running_sum = 0
        min_operation = float(inf)
        max_move = len(nums)
        
        for i in range(len(nums)):
            running_sum += nums[i]
            sum_at_each_position[running_sum] = i + 1
            
            if (x - (total_sum - running_sum)) in sum_at_each_position:
                left_rmove = sum_at_each_position[(x - (total_sum - running_sum))]
                right_rmove = max_move - i - 1
                min_operation = min(min_operation, right_rmove + left_rmove)

        return min_operation if min_operation != float(inf) else - 1
        