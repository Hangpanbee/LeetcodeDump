class Solution:
    def racecar(self, target: int) -> int:
        dp = {}
        
        q = collections.deque()
        q.append((0, 1, 0))
        dp2 = {}
        while q:
            pos, speed, count = q.popleft()
            
            reverseSpeed = -1 if speed >= 0 else 1
            for nextPos, nextSpeed, nextCount in [(pos+speed, speed*2, count+1), (pos, reverseSpeed, count+1)]:
                if (nextPos, nextSpeed) in dp: continue
                if abs(target-nextPos) > target: continue
                q.append((nextPos, nextSpeed, nextCount))
                if nextPos == target: return nextCount
          
                dp[(nextPos, nextSpeed)] = (nextCount)
           
