class Solution:
    def fallingSquares(self, positions):
        intervals = []
        res = []
        h = 0
        for pos in positions:
            st, en, height = pos[0], pos[0] + pos[1] - 1, pos[1]
            current = [st, en, height]
            prev_h = 0
            for interval in intervals:
                if st > interval[1]:continue
                if en < interval[0]:continue
                prev_h = max(prev_h, interval[2])
            current[2] += prev_h
            h = max(h, current[2])
            res.append(h)
            intervals.append(current)
        return res
                
                
        