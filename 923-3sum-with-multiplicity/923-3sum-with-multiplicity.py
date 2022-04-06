from math import comb
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = {}
        uniqueArray = []
        for i, v in enumerate(arr):
            if v not in counter:
                counter[v] = 1
                uniqueArray.append(v)
            else:
                counter[v] += 1

        uniqueArray.sort()
        arr = uniqueArray
        l, r = 0, len(arr)-1
        curr = 0
        ans = 0
        #print(arr, counter)
        while curr < len(arr):

            if l > curr or r < curr or l >= len(arr) or r < 0:
                curr += 1
                l,r = 0, len(arr) - 1
                continue
            currSum = arr[curr] + arr[l] + arr[r]
            if currSum == target:
                if l == curr == r: 
                    if counter[arr[curr]] >= 3:
                        #print(counter[arr[curr]], 'here')
                        ans += comb(counter[arr[curr]], 3)
                    
                elif l == curr:
                    if counter[arr[curr]] >= 2:
                        ans += comb(counter[arr[curr]], 2) * counter[arr[r]]
                    
                elif curr == r:
                    if counter[arr[curr]] >= 2:
                        #print('here', comb(counter[curr], 2), print(counter[curr]))
                        ans += comb(counter[arr[curr]], 2) * counter[arr[l]]
                elif l != curr != r:
                    ans += counter[arr[l]] * counter[arr[curr]] * counter[arr[r]]
    
                l += 1
                r -= 1
                #print(ans, l, r, curr)   
            elif currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            

            
        return ans % (10**9+7)
        