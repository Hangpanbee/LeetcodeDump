class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        ls = sorted(set([i  for d in events for i in {d[0]-1, d[1]}]))
        #print(ls)
        events =[[d[0]-1, d[1], d[2]]  for d in events]
        events.sort()
 
        memoize = {}
        curr_event = 0
        @lru_cache(None)
        def dp(k, limit, curr_event):
            if k == 0: return 0
            if curr_event >= len(events): return 0
            if (k, limit, curr_event) in memoize: return memoize[(k, limit, curr_event)]
            start, end, value = events[curr_event]
            take, notake = 0, 0
            if limit <= start:
                take = value + dp(k-1, end, curr_event+1)
            
            notake = dp(k, limit, curr_event+1)
            
            memoize[(k, limit, curr_event)] = max(take, notake)
           
            return memoize[(k, limit, curr_event)]
  
        return dp(k, -1, 0)
            
    
#    [[1,2,4],[3,4,7],[1,4,9],[5,6,3]]
#2