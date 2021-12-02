class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        map_val_to_index = collections.defaultdict(list)
        
        for i, v in enumerate(arr):
            map_val_to_index[v].append(i)
            
        arr.sort()
        rank = 1
        ans = [0]*len(arr)
        for num in arr:
            if num not in map_val_to_index: continue
            real_index_list = map_val_to_index[num]
            for index in real_index_list:
                ans[index] = rank
            del map_val_to_index[num]
            rank += 1
        return ans
                
            