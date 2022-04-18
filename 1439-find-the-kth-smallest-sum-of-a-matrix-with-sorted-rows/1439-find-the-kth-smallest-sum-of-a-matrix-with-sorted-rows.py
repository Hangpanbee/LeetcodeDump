class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        m,n = len(mat), len(mat[0])
        currSum = 0
        ans = []
        for r in range(m):
            currSum += mat[r][0]
        ans.append([currSum, [0]*m])
        heap = []
        heapq.heappush(heap, [currSum, [0]*m])
        
        i = 0
        seen = {}
 
        while heap:
            val, arr = heapq.heappop(heap)
            if tuple(arr) in seen: continue
            seen[tuple(arr)] = True
            i+=1
            #print(val, arr, i)
            if i == k: return val
            for r in range(m):
                if arr[r] + 1 >= n: continue
                arrCopy = arr.copy()
                arrCopy[r] += 1
                if tuple(arrCopy) in seen: continue
                heapq.heappush(heap, [val - mat[r][arrCopy[r]-1] + mat[r][arrCopy[r]], arrCopy])
                
            
           
        return val