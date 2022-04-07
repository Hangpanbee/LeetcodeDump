class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
  
        people = sorted(people, key= lambda x: (-x[0], x))
        for i, v in enumerate(people):
            ans.insert(v[1], v)
        print(ans)
        return ans
        
        