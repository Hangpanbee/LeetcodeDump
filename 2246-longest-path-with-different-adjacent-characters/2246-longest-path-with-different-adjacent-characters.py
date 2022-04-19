class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if len(s) == 1: return 1
        tree = collections.defaultdict(list)
        for i,v in enumerate(parent):
            tree[v].append(i)

        def helper(root):
            if tree[root]:          
                maxBranchDia = 0
                maxBranchHeight = 0
                secondMaxBranchHeight = 0
            
                for child in tree[root]:
                    aBranchDia, aBranchHeight = helper(child)
                    maxBranchDia = max(maxBranchDia, aBranchDia, aBranchHeight)
                    if s[child] != s[root]:                        
                        aBranchHeight += 1
                    else:
                        aBranchHeight = 0
                        aBranchDia = 0
            
                    if aBranchHeight > maxBranchHeight:
                        maxBranchHeight, secondMaxBranchHeight = aBranchHeight, maxBranchHeight
                    elif aBranchHeight > secondMaxBranchHeight:
                        secondMaxBranchHeight = aBranchHeight
  
                maxBranchDia = max(maxBranchDia,  1 + maxBranchHeight + secondMaxBranchHeight)
                
 
                
                return max(maxBranchDia, maxBranchHeight), maxBranchHeight
            else: return 0, 0
        a = helper(0)
        #print(a)
        return a[0]