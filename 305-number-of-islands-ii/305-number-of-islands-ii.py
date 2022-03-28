class DSU:
    def __init__(self, num):
        self.numIsl = 0
        self.par = list(range(num))
        self.rnk = [0] * num

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.numIsl -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        UF = DSU(m*n)
        i = 0
        ans = []
    
        visited = {}
        directs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while i < len(positions):
            r, c = positions[i]
            if (r, c) in visited: 
                ans.append(UF.numIsl)
                i+=1
                continue
            visited[(r, c)] = "1"
            UF.numIsl += 1
            for row, col in directs:
                new_row = r + row
                new_col = c + col
                if new_row < 0 or new_col < 0 or new_row >= m or new_col >= n:
                    continue
                flatten_rc = r*n + c    
                new_flatten_rc = new_row*n + new_col
                #print(new_row, new_col, positions)
                if (new_row, new_col) in visited:
                    UF.union(flatten_rc, new_flatten_rc)
                
            ans.append(UF.numIsl)
            i += 1
        return ans