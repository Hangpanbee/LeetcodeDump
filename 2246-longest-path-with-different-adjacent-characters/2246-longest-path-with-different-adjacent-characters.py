class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if len(s) == 1: return 1
        tree = collections.defaultdict(list)
        for i,v in enumerate(parent):
            tree[v].append(i)
        #print(tree)
            
        def helper(root):
            if tree[root]:          
                maxBranchDia = 0
                maxBranchHeight = 0
        
                branchHeight = []
            
                for child in tree[root]:
                    aBranchDia, aBranchHeight = helper(child)
                    maxBranchDia = max(maxBranchDia, aBranchDia, aBranchHeight)
                    if s[child] != s[root]:                        
                        aBranchHeight += 1
                    else:
                        aBranchHeight = 0
                        aBranchDia = 0
                    maxBranchDia = max(maxBranchDia, aBranchDia)
                    maxBranchHeight = max(maxBranchHeight, aBranchHeight)
                    #print('inside', child, aBranchHeight, aBranchDia)
                    branchHeight.append(aBranchHeight)
                if (len(branchHeight) < 2):
                    branchHeight.append(0)
                branchHeight.sort()
                if len(branchHeight) >= 2:
                    
                    maxBranchDia = max(maxBranchDia,  1 + branchHeight[-1] + branchHeight[-2])
                
                #print(maxBranchHeight, maxBranchDia, root)
                #print(branchHeight)
                
                return max(maxBranchDia, maxBranchHeight), maxBranchHeight
            else: return 0, 0
        a = helper(0)
        #print(a)
        return a[0]