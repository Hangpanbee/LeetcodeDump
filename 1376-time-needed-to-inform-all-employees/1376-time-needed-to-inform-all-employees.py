class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        max height of a tree with weight?
        """
        mapMtoS = collections.defaultdict(list)
        startTime = 0
        for s, m in enumerate(manager):
            mapMtoS[m].append(s)
            if m == -1: startTime = informTime[s]
        
        
        def dfs(curr):
            time = 0
            for s in mapMtoS[curr]:
                if curr == -1: iTime = startTime
                else: iTime = informTime[s]
                time = max(time,iTime+dfs(s))
            return time
        
        return dfs(-1)