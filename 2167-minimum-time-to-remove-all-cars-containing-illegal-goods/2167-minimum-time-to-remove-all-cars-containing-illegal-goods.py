class Solution:
    def minimumTime(self, s: str) -> int:
    
        illegal_cars = []
        for i,car in enumerate(s):
            if car == '1': illegal_cars.append(i)
        if len(illegal_cars) == 0: return 0

        left_moves = [0]*len(illegal_cars)
        right_moves = [0]*len(illegal_cars)
        
        for i, v in enumerate(illegal_cars):
            left_moves[i] = v + 1
            right_moves[i] = len(s) - v
            
        #take left
        for i, v in enumerate(left_moves):
            if i == 0:
                left_moves[i] = min(left_moves[i], 2)
            else:
                left_moves[i] = min(left_moves[i], left_moves[i-1]+2)
        #take right
        for i in range(len(right_moves)-1, -1, -1):
            if i == len(right_moves)-1:
                right_moves[i] = min(right_moves[i], 2)
            else:
                right_moves[i] = min(right_moves[i], right_moves[i+1]+2)
        max_num = min(left_moves[-1], right_moves[0])
        for i in range(len(illegal_cars)-1):
            max_num = min(left_moves[i]+right_moves[i+1], max_num)
        #print(left_moves, right_moves)
        return max_num