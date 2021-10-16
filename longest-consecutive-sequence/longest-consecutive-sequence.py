class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, num):
        parent = self.parent[num]
        if self.parent[num] != num:
            parent = self.find(self.parent[num])
        return parent
        
    def union(self, num1, num2):
        parentNum1 = self.find(num1)
        parentNum2 = self.find(num2)

        if self.rank[parentNum1] > self.rank[parentNum2]:
            self.parent[parentNum2] = self.parent[parentNum1]
            self.rank[parentNum1] += self.rank[parentNum2]
            return self.rank[parentNum1]
        else:
            self.parent[parentNum1] = self.parent[parentNum2]
            self.rank[parentNum2] += self.rank[parentNum1]
            return self.rank[parentNum1]
        
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remember this allow duplicates
        
        # ex: [0,1,7,200,100,9,6,12,8]
        # self.parent = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # self.size = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        # seen = {0: 0, 1: 1, 7: 2, 200: 3, 100: 4, 9: 5, 6: 6, 12: 7, 8: 8}
        if not len(nums): return 0
        
        nums = list(set(nums))
        disjointSet = DisjointSet(len(nums))
        seen = {}
        
        for numIndex in range(len(nums)):
            seen[nums[numIndex]] = numIndex

        

        for numIndex in range(len(nums)):
            num2 = nums[numIndex] + 1
            if (num2) in seen:
                disjointSet.union(seen[num2], numIndex)
            else: continue
        
        return max(disjointSet.rank)
                
        #1st: self.parent = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #end goal: self.parent = [1, 1, 8, 3, 4, 5, 2, 7, 5
        
        
        #for num in nums:
            #if num+1 in seen:
                #find self.parent[num+1] != self.parent[num];
                    #currSize = union(num+1, num)
                    #currMax = max(currSize, currMax)
            #else: continue
                    
        #1st: self.parent[0] != self.parent[1] -> currSuze = 2, currMax = 2
            #self.parent = [1, 1, 2, 3, 4, 5, 6, 7, 8]
            #self.rank =   [1, 2, 1, 1, 1, 1, 1, 1, 1]
        #2nd: self.parent[1] 
        #3rd: self.parent[2] != self.parent[8] -> currSize = 2, currMax = 2
            #self.parent = [1, 1, 8, 3, 4, 5, 6, 7, 8]
            #self.rank =   [1, 2, 1, 1, 1, 1, 1, 1, 2]
        #4th: self.parent[3]
        #5th: self.parent[4]
        #6th: self.parent[5]
        #7th: self.parent[6] (6) != self.parent[2] => 6 & 8
            #self.parent = [1, 1, 8, 3, 4, 5, 8, 7, 8]
            #self.rank =  [1, 2, 1, 1, 1, 1, 1, 1, 3]
        #8th: self.parent[7]
        #9th: self.parent[8] != self.parent[5]
            #self.parent = [1, 1, 8, 3, 4, 8, 8, 7, 8]
            #self.rank =   [1, 2, 1, 1, 1, 1, 1, 1, 4]
            
        
        
        
        