class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        kArray = [[] for i in range(len(nums)+1)]
        counter = {}
        
        for i, v in enumerate(nums):
            if v in counter:
                counter[v] += 1
            else:
                counter[v] = 1

        for k, v in counter.items():
            kArray[v].append(k)

        ans = []
        for i in range(len(kArray)-1, -1, -1):
            if not kArray[i]: continue
            ans.extend(kArray[i])
            if len(ans) == K: return ans
            elif len(ans) > K:
                while len(ans) > k: ans.pop()
                return ans