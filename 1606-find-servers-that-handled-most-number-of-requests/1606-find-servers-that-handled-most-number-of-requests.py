class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        free = list(range(k))
        jobCount = len(arrival)
        server = [0]*k
        # free = [0,1] jobCount = 4
        # server = [0,0]
        for i in range(jobCount):
            # i = 0
            # i = 1
            # i = 2
            # i = 3
            aTime = arrival[i]
            # aTime = 2
            # aTime = 3
            # aTime = 4
            # aTime = 8
            while busy and busy[0][0] <= aTime:
                eTime, freeS = heapq.heappop(busy)
                heapq.heappush(free, i + (freeS-i)%k)
            if not free: continue
            currServer = heapq.heappop(free) % k
            server[currServer] += 1
            # [1,1]
            heapq.heappush(busy, (aTime+load[i], currServer))
            # busy = [(5,0),(5,1)]
        busiestServer = max(server)
        ans = []
        #print(server)
        for i, s in enumerate(server):
            if s == busiestServer: ans.append(i)
        return ans